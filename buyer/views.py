from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from authentication.models import registerModel, AddressModel
from master.utils.n_RANDOM.otp import generate_otp
from master.utils.n_VALIDATORS.fields import is_valid_email, is_valid_password
from django.conf import settings
from .models import ContactModel, cartModel
from django.http import HttpResponse
from seller.models import productModel,categoryModel


import os

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'c_id' not in request.session:
            messages.warning(request, "You are not logged in.")
            return redirect('login_view')
        return view_func(request, *args, **kwargs)
    return wrapper

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        password_ = request.POST['password']
        confirm_password_ = request.POST['c_password']

        if is_valid_email(email_):
            if password_ == confirm_password_:
                is_valid_pwd, msg = is_valid_password(password_)
                if is_valid_pwd:
                    otp_ = generate_otp(6)
                    new_customer = registerModel.objects.create(
                        email = email_,
                        password = password_,
                        otp=otp_
                    )
                    new_customer.save()

                    subject = 'Your One-Time Password (OTP) | NEW-LOOK-OUTFITS'
                    message = f"""
                    Dear Customer,

                    Your One-Time Password (OTP) to verify your account is: {otp_}. Please use this code to proceed with the verification process.

                    Thank you.
                    """
                    # from_email = settings.EMAIL_HOST_USER
                    from_email = os.environ.get('EMAIL_HOST_USER')
                    recipient_list = [f'{email_}']
                    print(subject, message, from_email, recipient_list)
                    send_mail(subject, message, from_email, recipient_list)

                    context = {
                        'cum_email':email_
                    }
                    messages.warning(request, f"Please check your '{email_}' for the OTP. Enter the received OTP on this confirmation page to verify your email address.")
                    return render(request, 'buyer/otp_verification.html', context)
                else:
                    messages.warning(request, f"{msg}")
                    print(is_valid_password(password_))
                    return redirect('register_view')
            else:
                messages.warning(request, "Password and confirm password does not match.")
                return redirect('register_view')
        else:
            messages.warning(request, "Invalid Email.")
            return redirect('register_view')        
    return render(request, 'buyer/register.html')

def new_otp_verification(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        otp_ = request.POST['otp']
        if otp_.isdigit() and len(otp_) == 6:
            try:
                get_customer = registerModel.objects.get(email=email_)
            except registerModel.DoesNotExist:
                messages.warning(request, "User does not exist.")
                context = {
                    'cum_email': email_
                }
                return render(request, 'buyer/otp_verification.html', context)
            else:
                if get_customer.otp == otp_:
                    get_customer.is_activate = True
                    get_customer.save()
                    messages.success(request, 'Your email has been confirmed. Thank you!')
                    return redirect('login_view')
                else:
                    messages.warning(request, "Invalid OTP.")
                    context = {
                        'cum_email':email_
                    }
                    return render(request, 'buyer/otp_verification.html', context)
        else:
            messages.warning(request, "Invalid OTP input. OTP must be digit[0-9] or only 6 digit(length).")
            context = {
                'cum_email':email_
            }
            return render(request, 'buyer/otp_verification.html', context)


    return render(request, 'buyer/otp_verification.html')

@login_required
def cart_view(request):
    cartItems = cartModel.objects.filter(c_id_id=request.session['c_id'])
    print(cartItems)
    context = {
        'cartItems':cartItems
    }
    return render(request, 'buyer/cart.html',context)

def prodcut_cart(pro_id):
    return cartModel.objects.filter(pro_id=pro_id).exists()

@login_required
def add_item(request, pro_id):
    if not prodcut_cart(pro_id):
        new_cart_item = cartModel.objects.create(
            c_id_id=request.session['c_id'],
            pro_id_id=pro_id
        )
        new_cart_item.save()
        messages.success(request, "Added In Cart.")
    else:
        get_cart_item = cartModel.objects.get(pro_id_id=pro_id)
        get_cart_item.quantity += 1
        get_cart_item.save()
    
    return redirect('cart_view')


   
def login_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        password_ = request.POST['password']
        if is_valid_email(email_):
            try:
                get_customer = registerModel.objects.get(email=email_)
            except registerModel.DoesNotExist:
                messages.warning(request, "User does not exist.")
                return redirect('login_view')
            else:
                if get_customer:
                    if get_customer.password == password_:
                        print(get_customer.c_id, "Added")
                        request.session['c_id'] = get_customer.c_id
                        messages.success(request, " logged in Successfully.")
                        return redirect('index_view')
                    else:
                        messages.warning(request, "Email or Password does not matched.")
                        return redirect('login_view')
        else:
            messages.warning(request, " Email is not valid.")
            return redirect('login_view')        

    return render(request, 'buyer/login.html')

def forgot_password(request):
    return render(request, 'buyer/forgot.html')

def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        # Here you would implement the logic to reset the password and send instructions to the provided email.
        return HttpResponse("Password reset instructions sent to {}".format(email))
    else:
        return HttpResponse("Method not allowed", status=405)


@login_required
def logout(request):
  
    del request.session['c_id']
    messages.success(request, " you are logged out.")
    return redirect('login_view')

def index_view(request):
    return render(request, 'buyer/index.html')


def contact_view(request):
    if request.method == 'POST':
        fname_ = request.POST['first_name']
        lname_ = request.POST['last_name']
        email_ = request.POST['email']
        phone_ = request.POST['phone']
        msg_ = request.POST['message']

        if is_valid_email(email_):
            new_contact = ContactModel.objects.create(
                first_name=fname_,
                last_name=lname_,
                email=email_,
                phone=phone_,
                message=msg_
            )
            new_contact.save()
            messages.success(request, "Your request has been submited.")
            return redirect('contact_view')
        else:
            messages.warning(request, "Invalid email")
            return redirect('contact_view')
    return render(request, 'buyer/contact.html')
   

@login_required
def profile_view(request):
    if 'c_id' in request.session:
        c_id_ = request.session['c_id']
        get_customer = registerModel.objects.get(c_id=c_id_)
        try:
            get_address = AddressModel.objects.get(c_id=c_id_)
        except:
            get_address = False
    
        context = {
            'get_customer':get_customer,
            'get_address':get_address
        }
        return render(request, 'buyer/profile.html', context)
    else:
        print("Your Customer ID does not exist in the session")
        return redirect('login_view')

def update_info(request):
    print("here....")
    if request.method == 'POST':
        first_name_ = request.POST['firstname']
        last_name_ = request.POST['lastname']
        mobile_ = request.POST['mobile']

        try:
            get_customer = get_object_or_404(registerModel, c_id=request.session['c_id'])
        except registerModel.DoesNotExist:
            messages.warning(request, 'User does not existed.')
            return redirect('profile_view')
        else:
            get_customer.first_name = first_name_
            get_customer.last_name = last_name_
            get_customer.mobile = mobile_
            get_customer.save()
            messages.success(request, 'Your Profile Is updated.')
            return redirect('profile_view')

def shopping_view(request):
    categoris = categoryModel.objects.all()
    products = productModel.objects.all()
    context = {
        'products':products,
        'categoris':categoris
    }
    return render(request, "buyer/shopping.html", context)


