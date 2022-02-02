from django.shortcuts import render
from .models import *
from .utils import *
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
import random
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        context ={
            'usercount':user.objects.all().count(),
            'membercount':s_member.objects.all().count(),
            'chairmancount':chairman.objects.all().count(),
            'watchmancount':watchman.objects.all().count(), 
            'user':user_id
        }
        if user_id.role=='member':
            mid=s_member.objects.get(user_id=user_id)
            context['user']=mid
            return render(request,'index.html',context)
        elif user_id.role=='chairman':
            cid=chairman.objects.get(user_id=user_id)
            context['user']=cid
            return render(request,'index.html',context)
        elif user_id.role=='watchman':
            wid=watchman.objects.get(user_id=user_id)
            context['user']=wid
            return render(request,'index.html',context)
    else:
        return render(request,'login.html')

def main(request):
    return render(request,'main.html')

def registration(request):
    if request.method=='POST':
        role=request.POST['role']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['confirmpassword']
        if c_password==password:
            uid=user.objects.create(role=role,
                                    first_name=fname,
                                    last_name=lname,
                                    email=email,
                                    password=password)
            uid=user.objects.get(email=email) 
            if role=='member':
                mid=s_member.objects.create(user_id=uid,first_name=fname,last_name=lname,email=email)
                print("--------------------->",email)
                sendmail('conformation','mail',email,{'firstname':fname,'lastname':lname})
                return render(request,'login.html')
            elif role=='chairman':
                cid=chairman.objects.create(user_id=uid,first_name=fname,last_name=lname,email=email)
                sendmail('conformation','mail',email,{'firstname':fname,'lastname':lname})
                return render(request,'login.html')
            elif role=='watchman':
                wid=watchman.objects.create(user_id=uid,first_name=fname,last_name=lname,email=email)
                sendmail('conformation','mail',email,{'firstname':fname,'lastname':lname})
                return render(request,'login.html')
        else:
            msg="password and confirm password must be same"
            return render(request,'registration.html',{'msg':msg})
    else:
        if 'email' in request.session:
            user_id=user.objects.get(email=request.session['email'])
            return render(request,'index.html',{'user':user_id})
        else:
            return render(request,'registration.html')

@csrf_exempt
def login(request):
    if request.method=='POST':
        # role=request.POST['role']
        email=request.POST['email']
        password=request.POST['password']
        user_id=user.objects.get(email=email)
        if user_id.password==password:
            context ={
            'usercount':user.objects.all().count(),
            'membercount':s_member.objects.all().count(),
            'chairmancount':chairman.objects.all().count(),
            'watchmancount':watchman.objects.all().count(), 
            'user':user_id
            }
            request.session['email']=user_id.email
            if user_id.role=='chairman':
                cid=chairman.objects.get(user_id=user_id)
                context['user']=cid
                return render(request,'index.html',context)
            elif user_id.role=='member':
                mid=s_member.objects.get(user_id=user_id)
                context['user']=mid
                return render(request,'index.html',context)
            elif user_id.role=='watchman':
                wid=watchman.objects.get(user_id=user_id)
                context['user']=wid
                return render(request,'index.html',context)
            else:
                msg="incorrect details"
                return render(request,'login.html',{'msg':msg})      
        else:
            msg="incorrect details"
            return render(request,'login.html',{'msg':msg})      
    else:
        if 'email' in request.session:
            user_id = user.objects.filter(email=request.session['email'])
            if user_id.role=='chairman':
                cid=chairman.objects.get(user_id=user_id)
                return render(request,'index.html',{'user':cid})
            elif user_id.role=='member':
                mid=s_member.objects.get(user_id=user_id)
                return render(request,'index.html',{'user':mid})
            elif user_id.role=='watchman':
                wid=watchman.objects.get(user_id=user_id)
                return render(request,'index.html',{'user':wid})
            else:
                msg="incorrect details"
                return render(request,'login.html',{'msg':msg})
        else:
            return render (request,'login.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,'login.html')
    else:
        return render(request,'login.html')

def profile(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        context ={
            'usercount':user.objects.all().count(),
            'membercount':s_member.objects.all().count(),
            'chairmancount':chairman.objects.all().count(),
            'watchmancount':watchman.objects.all().count(), 
            'user':user_id
        }
        if user_id.role=='member':
            mid=s_member.objects.get(user_id=user_id)
            context['user']=mid
            return render(request,'profile.html',context)
        elif user_id.role=='chairman':
            cid=chairman.objects.get(user_id=user_id)
            context['user']=cid
            return render(request,'profile.html',context)
        elif user_id.role=='watchman':
            wid=watchman.objects.get(user_id=user_id)
            context['user']=wid
            return render(request,'profile.html',context)
    else:
        return render(request,'login.html')

def edit_profile(request):
    if request.method=="POST":
        dob=request.POST['dob']
        gender=request.POST['gender']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        phonenumber=request.POST['phonenumber']
        flatno=request.POST['flatno']
        user_id=user.objects.get(email=request.session['email'])
        context ={
            'usercount':user.objects.all().count(),
            'membercount':s_member.objects.all().count(),
            'chairmancount':chairman.objects.all().count(),
            'watchmancount':watchman.objects.all().count(), 
            'user':user_id
        }
        if user_id.role=='member':
            mid=s_member.objects.get(user_id=user_id)
            mid.dob=dob
            mid.gender=gender
            mid.address=address
            mid.state=state
            mid.country=country
            mid.pincode=pincode
            mid.phone_number=phonenumber
            mid.flat_no=flatno
            mid.save()
            context['user']=mid
            return render(request,'profile.html',context)
        elif user_id.role=='chairman':
            cid=chairman.objects.get(user_id=user_id)
            cid.dob=dob
            cid.gender=gender
            cid.address=address
            cid.state=state
            cid.country=country
            cid.pincode=pincode
            cid.phone_number=phonenumber
            cid.flat_no=flatno
            cid.save()
            context['user']=cid
            return render(request,'profile.html',context)
        elif user_id.role=='watchman':
            wid=watchman.objects.get(user_id=user_id)
            wid.dob=dob
            wid.gender=gender
            wid.address=address
            wid.state=state
            wid.country=country
            wid.pincode=pincode
            wid.phone_number=phonenumber
            wid.flat_no=flatno
            wid.save()
            context['user']=wid
            return render(request,'profile.html',context)
    else:
        if 'email' in request.session:
            user_id = user.objects.get(email=request.session['email'])
            context ={
                'usercount':user.objects.all().count(),
                'membercount':s_member.objects.all().count(),
                'chairmancount':chairman.objects.all().count(),
                'watchmancount':watchman.objects.all().count(), 
                'user':user_id
            }
            if user_id.role=='member':
                mid=s_member.objects.get(user_id=user_id)
                context['user']=mid
                return render(request,'profile.html',context)
            elif user_id.role=='chairman':
                cid=chairman.objects.get(user_id=user_id)
                context['user']=cid
                return render(request,'profile.html',context)
            elif user_id.role=='watchman':
                wid=watchman.objects.get(user_id=user_id)
                context['user']=wid
                return render(request,'profile.html',context)
        else:
            return render(request,'login.html')

def add_visitor(request):
    if request.method=="POST":
        name=request.POST['name']
        phonenumber=request.POST['phonenumber']
        flatno=request.POST['flatno']
        # date=datetime.datetime.now().date
        # time=datetime.datetime.now().time
        user_id=user.objects.get(email=request.session['email'])
        all_visitors=visitor.objects.all()
        context ={
            'user':user_id,
            'visitor':all_visitors,
        }
        vid=visitor.objects.create(name=name,phone_number=phonenumber,flat_no=flatno)
        return render(request,'allvisitor.html',context)
    else:
        if 'email' in request.session:
            user_id = user.objects.get(email=request.session['email'])
            context ={
                'usercount':user.objects.all().count(),
                'membercount':s_member.objects.all().count(),
                'chairmancount':chairman.objects.all().count(),
                'watchmancount':watchman.objects.all().count(), 
                'user':user_id,
                
            }
            if user_id.role=='member':
                mid=s_member.objects.get(user_id=user_id)
                context['user']=mid
                return render(request,'allvisitor.html',context)
            elif user_id.role=='chairman':
                cid=chairman.objects.get(user_id=user_id)
                context['user']=cid
                return render(request,'allvisitor.html',context)
            elif user_id.role=='watchman':
                wid=watchman.objects.get(user_id=user_id)
                context['user']=wid
                return render(request,'allvisitor.html',context)
        else:
            return render(request,'login.html')

def member(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        all_chairman=chairman.objects.all()
        all_member=s_member.objects.all()
        all_watchman=watchman.objects.all()
        all_user=user.objects.all()
        context={
            'chairman':all_chairman,
            'watchman':all_watchman,
            'member':all_member,
            'user':all_user
        }
        if user_id.role=='chairman':
            cid=chairman.objects.get(user_id=user_id)
            context['user']=cid
            return render(request,'member.html',context)
        elif user_id.role=='member':
            mid=s_member.objects.get(user_id=user_id)
            context['user']=mid
            return render(request,'member.html',context)
        elif user_id.role=='watchman':
            wid=watchman.objects.get(user_id=user_id)
            context['user']=wid
            return render(request,'member.html',context)
        else:
            return render(request,'login.html')
    else:
        return render (request,'login.html')

def maintenance(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        all_chairman=chairman.objects.all()
        all_member=s_member.objects.all()
        all_watchman=watchman.objects.all()
        all_user=user.objects.all()
        context={
            'chairman':all_chairman,
            'watchman':all_watchman,
            'member':all_member,
            'user':all_user
        }
        if user_id.role=='chairman':
            cid=chairman.objects.get(user_id=user_id)
            context['user']=cid
            return render(request,'maintenance.html',context)
        elif user_id.role=='member':
            mid=s_member.objects.get(user_id=user_id)
            context['user']=mid
            return render(request,'maintenance.html',context)
        elif user_id.role=='watchman':
            wid=watchman.objects.get(user_id=user_id)
            context['user']=wid
            return render(request,'maintenance.html',context)
        else:
            return render(request,'login.html')
    else:
        return render (request,'login.html')

def add_complaint(request):
    if request.method=="POST":
        email=request.POST['email']
        flatno=request.POST['flatno']
        c_subject=request.POST['c_subject']
        c_discription=request.POST['c_discription']
        user_id=user.objects.get(email=request.session['email'])
        allcomplaint=comp_details.objects.all()
        context ={
            'user':user_id,
            'complaint':allcomplaint
        }
        cid=comp_details.objects.create(flat_no=flatno,c_subject=c_subject,c_discription=c_discription,email=email,)
        return render(request,'allcomplaint.html',context)
    else:
        if 'email' in request.session:
            user_id = user.objects.get(email=request.session['email'])
            context ={
                'usercount':user.objects.all().count(),
                'membercount':s_member.objects.all().count(),
                'chairmancount':chairman.objects.all().count(),
                'watchmancount':watchman.objects.all().count(), 
                'user':user_id,
                
            }
            if user_id.role=='member':
                mid=s_member.objects.get(user_id=user_id)
                context['user']=mid
                return render(request,'allcomplaint.html',context)
            elif user_id.role=='chairman':
                cid=chairman.objects.get(user_id=user_id)
                context['user']=cid
                return render(request,'allcomplaint.html',context)
            elif user_id.role=='watchman':
                wid=watchman.objects.get(user_id=user_id)
                context['user']=wid
                return render(request,'allcomplaint.html',context)
        else:
            return render(request,'login.html')

def add_suggestion(request):
    if request.method=="POST":
        email=request.POST['email']
        flatno=request.POST['flatno']
        s_subject=request.POST['s_subject']
        s_discription=request.POST['s_discription']
        user_id=user.objects.get(email=request.session['email'])
        allsuggestion=sugg_details.objects.all()
        context ={
            'user':user_id,
            'suggestion':allsuggestion,
        }
        cid=sugg_details.objects.create(flat_no=flatno,s_subject=s_subject,s_discription=s_discription,email=email,)
        return render(request,'allsuggestion.html',context)
    else:
        if 'email' in request.session:
            user_id = user.objects.get(email=request.session['email'])
            context ={
                'usercount':user.objects.all().count(),
                'membercount':s_member.objects.all().count(),
                'chairmancount':chairman.objects.all().count(),
                'watchmancount':watchman.objects.all().count(), 
                'user':user_id,
            }
            if user_id.role=='member':
                mid=s_member.objects.get(user_id=user_id)
                context['user']=mid
                return render(request,'allsuggestion.html',context)
            elif user_id.role=='chairman':
                cid=chairman.objects.get(user_id=user_id)
                context['user']=cid
                return render(request,'allsuggestion.html',context)
            elif user_id.role=='watchman':
                wid=watchman.objects.get(user_id=user_id)
                context['user']=wid
                return render(request,'allsuggestion.html',context)
        else:
            return render(request,'login.html')

def alluser(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        all_chairman=chairman.objects.all()
        all_member=s_member.objects.all()
        all_watchman=watchman.objects.all()
        all_user=user.objects.all()
        context={
            'chairman':all_chairman,
            'watchman':all_watchman,
            'member':all_member,
            'user':all_user
        }
        if user_id.role=='chairman':
            cid=chairman.objects.get(user_id=user_id)
            context['user']=cid
            return render(request,'alluser.html',context)
        elif user_id.role=='member':
            mid=s_member.objects.get(user_id=user_id)
            context['user']=mid
            return render(request,'alluser.html',context)
        elif user_id.role=='watchman':
            wid=watchman.objects.get(user_id=user_id)
            context['user']=wid
            return render(request,'alluser.html',context)
        else:
            return render(request,'login.html')
    else:
        return render (request,'login.html')

def allvisitor(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        all_visitors=visitor.objects.all()
        context={
            'visitor':all_visitors,
            'user':user_id,
        }
        return render(request,'allvisitor.html',context)
    else:
        return render (request,'login.html')

def photos(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        all_chairman=chairman.objects.all()
        all_member=s_member.objects.all()
        all_watchman=watchman.objects.all()
        all_user=user.objects.all()
        context={
            'chairman':all_chairman,
            'watchman':all_watchman,
            'member':all_member,
            'user':all_user
        }
        if user_id.role=='chairman':
            cid=chairman.objects.get(user_id=user_id)
            context['user']=cid
            return render(request,'photos.html',context)
        elif user_id.role=='member':
            mid=s_member.objects.get(user_id=user_id)
            context['user']=mid
            return render(request,'photos.html',context)
        elif user_id.role=='watchman':
            wid=watchman.objects.get(user_id=user_id)
            context['user']=wid
            return render(request,'photos.html',context)
        else:
            return render(request,'login.html')
    else:
        return render (request,'login.html')

def videos(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        all_chairman=chairman.objects.all()
        all_member=s_member.objects.all()
        all_watchman=watchman.objects.all()
        all_user=user.objects.all()
        context={
            'chairman':all_chairman,
            'watchman':all_watchman,
            'member':all_member,
            'user':all_user
        }
        if user_id.role=='chairman':
            cid=chairman.objects.get(user_id=user_id)
            context['user']=cid
            return render(request,'videos.html',context)
        elif user_id.role=='member':
            mid=s_member.objects.get(user_id=user_id)
            context['user']=mid
            return render(request,'videos.html',context)
        elif user_id.role=='watchman':
            wid=watchman.objects.get(user_id=user_id)
            context['user']=wid
            return render(request,'videos.html',context)
        else:
            return render(request,'login.html')
    else:
        return render (request,'login.html')

def notice(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        nid = notice_details.objects.all()
        context={
            'user':user_id,
            'notice':nid,
        }
        return render(request,'notice.html',context)
    else:
        return render (request,'login.html')

def getpdf(request): 
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email']) 
        response = HttpResponse(content_type='application/pdf')  
        response['Content-Disposition'] = 'attachment; filename="Maintenance.pdf"'  
        p = canvas.Canvas(response)  
        p.setFont("Times-Roman",25)  
        p.drawString(60,700,'Email = {}'.format(request.session['email']))
        p.drawString(60,650,'name = {}'.format(user_id.first_name))
        p.drawString(60,600,'Maitenance = 15000')
        p.drawString(60,550,'Your maintenance has paid by {}'.format(user_id.first_name))
        p.showPage()  
        p.save()  
        return response  
    else:
        return render(request,'login.html')

def allcomplaint(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        all_complaint=comp_details.objects.all()
        context={
            'complaint':all_complaint,
            'user':user_id,
        }
        return render(request,'allcomplaint.html',context)
    else:
        return render (request,'login.html')

def allsuggestion(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        all_suggestion=sugg_details.objects.all()
        context={
            'suggestion':all_suggestion,
            'user':user_id,
        }
        return render(request,'allsuggestion.html',context)
    else:
        return render (request,'login.html')

def event(request):
    if 'email' in request.session:
        user_id = user.objects.get(email=request.session['email'])
        eid=event_details.objects.all()
        context={
            'user':user_id,
            'event':eid
        }
        return render(request,'event.html',context)
    else:
        return render (request,'login.html')

def forgotpassword(request):
    if request.method=='POST':
        email=request.POST['email']
        user_id=user.objects.filter(email=email)
        if user_id:
            user_id=user.objects.get(email=email)
            otp=random.randint(111111,999999)
            user_id.otp=otp
            user_id.save()
            sendmail('OTP','f_mail',email,{'otp':otp})
            return render(request,'new_password.html',{'email':email})
        else:
            msg='email does not exist'
            return render(request,'forgot_password.html',{'msg':msg})
    else:
        return render(request,'forgot_password.html')

def newpassword(request):
    if request.method=='POST':
        email=request.POST['email']
        otp=request.POST['otp']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        user_id=user.objects.get(email=email)
        if user_id.otp==int(otp):
            if password==confirmpassword:
                user_id.password=password
                user_id.save()
                return render(request,'login.html')
            else:
                msg="password and confirm password does not same"
                return render(request,'new_password.html',{'msg':msg})
        else:
            msg="incorrect otp"
            return render(request,'new_password.html',{'msg':msg})
    else:
        return render(request,'new_password.html')

def add_notice(request):
    if request.method=="POST":
        name=request.POST['name']
        n_subject=request.POST['n_subject']
        n_discription=request.POST['n_discription']
        user_id=user.objects.get(email=request.session['email'])
        nid=notice_details.objects.all()
        context ={
            'user':user_id,
            'notice':nid,
        }
        nid=notice_details.objects.create(name=name,n_subject=n_subject,n_discription=n_discription)
        return render(request,'notice.html',context)
    else:
        if 'email' in request.session:
            user_id = user.objects.get(email=request.session['email'])
            context ={
                'usercount':user.objects.all().count(),
                'membercount':s_member.objects.all().count(),
                'chairmancount':chairman.objects.all().count(),
                'watchmancount':watchman.objects.all().count(), 
                'user':user_id,
            }
            if user_id.role=='member':
                mid=s_member.objects.get(user_id=user_id)
                context['user']=mid
                return render(request,'notice.html',context)
            elif user_id.role=='chairman':
                cid=chairman.objects.get(user_id=user_id)
                context['user']=cid
                return render(request,'notice.html',context)
            elif user_id.role=='watchman':
                wid=watchman.objects.get(user_id=user_id)
                context['user']=wid
                return render(request,'notice.html',context)
        else:
            return render(request,'login.html')

def add_event(request):
    if request.method=="POST":
        m_name=request.POST['m_name']
        e_name=request.POST['e_name']
        e_date=request.POST['e_date']
        e_discription=request.POST['e_discription']
        user_id=user.objects.get(email=request.session['email'])
        eid=event_details.objects.all()
        context ={
            'user':user_id,
            'event':eid,
        }
        eid=event_details.objects.create(m_name=m_name,e_name=e_name,e_date=e_date,e_discription=e_discription)
        return render(request,'event.html',context)
    else:
        if 'email' in request.session:
            user_id = user.objects.get(email=request.session['email'])
            context ={
                'usercount':user.objects.all().count(),
                'membercount':s_member.objects.all().count(),
                'chairmancount':chairman.objects.all().count(),
                'watchmancount':watchman.objects.all().count(), 
                'user':user_id,
            }
            if user_id.role=='member':
                mid=s_member.objects.get(user_id=user_id)
                context['user']=mid
                return render(request,'event.html',context)
            elif user_id.role=='chairman':
                cid=chairman.objects.get(user_id=user_id)
                context['user']=cid
                return render(request,'event.html',context)
            elif user_id.role=='watchman':
                wid=watchman.objects.get(user_id=user_id)
                context['user']=wid
                return render(request,'event.html',context)
        else:
            return render(request,'login.html')
