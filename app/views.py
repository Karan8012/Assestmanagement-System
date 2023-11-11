from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict

from .models import *
import hashlib
import sweetify


# Create your views here.
def index(request):
    l = Employee.objects.all()
    p = len(l)
    com = Com.objects.all()
    cl = len(com)
    lap = Lap.objects.all()
    lp = len(lap)
    ass = Assest.objects.all()
    asse = len(ass)
    if 'email' in request.session:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        return render(request, 'index.html', {'user': u, 'emp': p, 'pos': pos, 'com': cl, 'lap': lp, 'ass': asse})
    else:
        return render(request, 'index.html', {'user': None, 'emp': p, 'pos': None, 'com': cl, 'lap': lp, 'ass': asse})


def register(request):
    if request.method == "POST":
        user = request.POST.get('user')
        email = request.POST.get('email')
        mobno = request.POST.get('mobno')
        postion = request.POST.get('postion')
        staffid = request.POST.get('staffid')
        pasw = request.POST.get('pasw')
        spasw = hashlib.md5(pasw.encode()).hexdigest()
        a = Register.objects.filter(email=email)
        b = []
        for i in a:
            em = i.email
            b.append(em)
        if a is not None and email not in b:
            reg = Register(user=user, email=email, mobno=mobno, postion=postion, staffid=staffid, pasw=spasw)
            reg.save()
            sweetify.success(request, title="Success", text="Register Successfull", timer=2000)
            return redirect('index')
        else:
            sweetify.error(request, title="Error", text="User Has Already Exists", timer=2000)
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pasw = request.POST.get('pasw')
        spasw = hashlib.md5(pasw.encode()).hexdigest()
        try:
            a = Register.objects.get(email=email)
            print(a.pasw)
            if a.pasw == spasw:
                request.session['email'] = email
                sweetify.success(request, title='Success', text='Login Successfully', timer=2000)
                return redirect('index')
            else:
                sweetify.error(request, title='Error', text='Email and Password Does not match', timer=2000)
        except:
            sweetify.error(request, 'User Account Does Not Exists')
    return render(request, 'signin.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('index')


def addemp(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        if request.method == 'POST':
            empname = request.POST.get('empname')
            empemail = request.POST.get('empemail')
            empdob = request.POST.get('empdob')
            empmbno = request.POST.get('empmbno')
            empage = request.POST.get('empage')
            empid = request.POST.get('empid')
            emppos = request.POST.get('emppos')
            empjndt = request.POST.get('empjndt')
            empexp = request.POST.get('empexp')
            emp = Employee(empname=empname, empemail=empemail, empdob=empdob, empmbno=empmbno, empage=empage,
                           empid=empid, emppos=emppos, empjndt=empjndt, empexp=empexp)
            emp.save()
            sweetify.success(request, title='success', text='Employee Details Register Successfully', timer=2000)
            return redirect('index')
        return render(request, 'addemp.html', {'user': u, 'pos': pos})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})


def comcat(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        com = Com.objects.all().filter()
        return render(request, 'comcat.html', {'user': u, 'pos': pos, 'com': com})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})


def comedit(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        if request.method == "POST":
            comname = request.POST.get('comname')
            os = request.POST.get('os')
            hdd = request.POST.get('hdd')
            ram = request.POST.get('ram')
            cpnm = request.POST.get('cpnm')
            cpsn = request.POST.get('cpsn')
            monname = request.POST.get('monname')
            mnsn = request.POST.get('mnsn')
            prcl = request.POST.get('prcl')
            grcname = request.POST.get('grcname')
            gcs = request.POST.get('gcs')
            kyname = request.POST.get('kyname')
            msname = request.POST.get('msname')
            com = Com(comname=comname, os=os, hdd=hdd, ram=ram, cpnm=cpnm, cpsn=cpsn, monname=monname, mnsn=mnsn,
                      prcl=prcl, grcname=grcname, gcs=gcs, kyname=kyname, msname=msname)
            com.save()
            sweetify.success(request, title='success', text='Computer Details Register Successfully', timer=2000)
            return redirect('comcat')
        return render(request, 'comedit.html', {'user': u, 'pos': pos})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})


def lapcat(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        lap = Lap.objects.all().filter()
        return render(request, 'lapcat.html', {'user': u, 'pos': pos, 'lap': lap})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})


def lapedit(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        if request.method == "POST":
            lapname = request.POST.get('lapname')
            los = request.POST.get('los')
            lhdd = request.POST.get('lhdd')
            lram = request.POST.get('lram')
            lcm = request.POST.get('lcm')
            lsn = request.POST.get('lsn')
            prcl = request.POST.get('prcl')
            grcname = request.POST.get('grcname')
            gcs = request.POST.get('gcs')
            canv = None
            canvs = request.POST.get('canv')
            canvss = request.POST.get('canvs')
            if bool(canvs) is False and bool(canvss) is True:
                canv = 'No'
            else:
                canv = canvs
            print(canv)
            lap = Lap(lapname=lapname, los=los, lhdd=lhdd, lram=lram, lcm=lcm, lsn=lsn, prcl=prcl, grcname=grcname,
                      gcs=gcs, canv=canv)
            lap.save()
            sweetify.success(request, title='success', text='Laptop Details Register Successfully', timer=2000)
            return redirect('lapcat')
        return render(request, 'lapedit.html', {'user': u, 'pos': pos})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})


def otheracc(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        oth = Otheracc.objects.all().filter()
        return render(request, 'othcat.html', {'user': u, 'pos': pos, 'oth': oth})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})


def otheraccedit(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        if request.method == "POST":
            keyboard = request.POST.get('keyboard')
            mouse = request.POST.get('mouse')
            other = request.POST.get('other')
            ok=Otheracc.objects.all().filter(keyboard=keyboard)
            p=[]
            for i in ok:
                p.append(i.keyboard)
            print(p)
            m=[]
            om=Otheracc.objects.all().filter(mouse=mouse)
            for i in om:
                m.append(i.mouse)
            print(m)
            o=[]
            oo=Otheracc.objects.all().filter(other=other)
            for i in oo:
                o.append(i.keyboard)
            print(o)
            if keyboard:
                if keyboard not in p:
                    oth = Otheracc(keyboard=keyboard)
                    oth.save()
                    sweetify.success(request, title='success', text='Other Accessories Register Successfully',
                                     timer=2000)
                else:
                    sweetify.error(request, title='error', text=f'That {keyboard} has already exists please Given Other name')
            elif mouse:
                if mouse not in m:
                    oth = Otheracc(mouse=mouse)
                    oth.save()
                    sweetify.success(request, title='success', text='Other Accessories Register Successfully',
                                     timer=2000)
                else:
                    sweetify.error(request, title='error', text=f'That {mouse} has already exists please Given Other name')
            elif other:
                if other not in o:
                    oth = Otheracc(other=other)
                    oth.save()
                    sweetify.success(request, title='success', text=f'{other} Register Successfully',
                                     timer=2000)
                else:
                    sweetify.error(request, title='error', text=f'That {other} has already exists please Given Other name')
            return redirect('otheracc')
        return render(request, 'otheraccedit.html', {'user': u, 'pos': pos})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})


def viewemployee(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        emp = Employee.objects.all().filter()
        return render(request, 'viewemployee.html', {'user': u, 'pos': pos, 'e': emp})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})

def addotherass(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        emp = Employee.objects.all().filter()
        oth = Otheracc.objects.all().filter()
        if request.method == 'POST':
            empls = request.POST.get('empls')
            otls = request.POST.get('otls')
            gdt = request.POST.get('gdt')
            rdt = request.POST.get('rdt')
            if otls != 'None':
                for i in oth:
                    if otls == i.keyboard:
                        oi = Otheracc.objects.get(keyboard=otls)
                        oi.delete()
                        ok=retOtheracc(empname=empls,keyboard=otls)
                        ok.save()
                        break

                    if otls == i.mouse:
                        omm = Otheracc.objects.get(mouse=otls)
                        omm.delete()
                        om = retOtheracc(empname=empls, mouse=otls)
                        om.save()
                        break

                    if otls == i.other:
                        ooo = Otheracc.objects.get(other=otls)
                        print(otls)
                        ooo.delete()
                        oo = retOtheracc(empname=empls, other=otls)
                        oo.save()
                        break
            if gdt != rdt:
                print(empls,otls,gdt,rdt)
                aast=reass(empls=empls,otls=otls,gdt=gdt,rdt=rdt)
                aast.save()
                sweetify.success(request, title='success', text='add Other accessories Successfully', timer=2000)
                return redirect('index')
            else:
                sweetify.error(request, title='error', text=f'Given Date and Return Data Has Same ({gdt}=={rdt})', timer=3000)
        return render(request, 'addass.html', {'user': u, 'pos': pos,'oth':oth,'emp':emp})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})

def addassests(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        emp = Employee.objects.all().filter()
        lap = Lap.objects.all().filter()
        com = Com.objects.all().filter()
        oth = Otheracc.objects.all().filter()
        if request.method == 'POST':
            empls = request.POST.get('empls')
            cmpls = request.POST.get('cmpls')
            lpls = request.POST.get('lpls')
            gdt = request.POST.get('gdt')
            rdt = request.POST.get('rdt')
            systy = None
            recom = Returncom.objects.all().filter(empname=empls)
            relap=returnlap.objects.all().filter(empname=empls)
            rec=[]
            rlp=[]
            for i in recom:
                rec.append(i.empname)
            for i in relap:
                rlp.append(i.empname)
            if cmpls != 'None':
                if empls in rec or empls in rlp:
                    sweetify.error(request,title='error',text=f'{empls} already got the Computer or laptop',timer=3000)
                    return redirect('/')
                else:
                    systy=cmpls
                    cm=Com.objects.all().filter(comname=cmpls)
                    for i in cm:
                        # print(i)
                        dt=Returncom(empname=empls,comname=i.comname,os=i.os, hdd=i.hdd, ram=i.ram, cpnm=i.cpnm, cpsn=i.cpsn,
                                   monname=i.monname, mnsn=i.mnsn, prcl=i.prcl, grcname=i.grcname, gcs=i.gcs,
                                   kyname=i.kyname, msname=i.msname)
                        dt.save()
                        cmm=Com.objects.get(comname=cmpls)
                        cmm.delete()
                        print('cmpls')
            if lpls != 'None':
                if empls in rlp or empls in rec:
                    sweetify.error(request,title='error',text=f'{empls} already got the Computer or laptop',timer=3000)
                    return redirect('/')
                else:
                    systy=lpls
                    lps=Lap.objects.all().filter(lapname=lpls)
                    for i in lps:
                        # print(i)
                        dl=returnlap(empname=empls,lapname=i.lapname, los=i.los, lhdd=i.lhdd, lram=i.lram, lcm=i.lcm, lsn=i.lsn,
                                   prcl=i.prcl, grcname=i.grcname, gcs=i.gcs, canv=i.canv)
                        dl.save()
                        lpp=Lap.objects.get(lapname=lpls)
                        lpp.delete()
                        print('lpls')
            if gdt != rdt:
                print(empls,systy,gdt,rdt)
                aast=Assest(empls=empls,systy=systy,gdt=gdt,rdt=rdt)
                aast.save()
                sweetify.success(request, title='success', text='Assest Register Successfully', timer=2000)
                return redirect('viewass')
            else:
                sweetify.error(request, title='error', text=f'Given Date and Return Data Has Same ({gdt}=={rdt})', timer=3000)
        return render(request, 'addassests.html',
                      {'user': u, 'pos': pos, 'emp': emp, 'com': com, 'lap': lap, 'oth': oth})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})


def viewass(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        ass = Assest.objects.all().filter()
        accem = reass.objects.all().filter()
        return render(request, 'viewass.html', {'user': u, 'pos': pos, 'ass': ass,'oass':accem})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})
def addass(request,id):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        oth = Otheracc.objects.all().filter()
        p=Assest.objects.get(id=id)
        if request.method == 'POST':
            empls = request.POST.get('empls')
            otls = request.POST.get('otls')
            gdt = request.POST.get('gdt')
            rdt = request.POST.get('rdt')
            if otls != 'None':
                for i in oth:
                    if otls == i.keyboard:
                        oi = Otheracc.objects.get(keyboard=otls)
                        oi.delete()
                        ok=retOtheracc(empname=empls,keyboard=otls)
                        ok.save()
                        break

                    if otls == i.mouse:
                        omm = Otheracc.objects.get(mouse=otls)
                        omm.delete()
                        om = retOtheracc(empname=empls, mouse=otls)
                        om.save()
                        break

                    if otls == i.other:
                        ooo = Otheracc.objects.get(other=otls)
                        print(otls)
                        ooo.delete()
                        oo = retOtheracc(empname=empls, other=otls)
                        oo.save()
                        break
            if gdt != rdt:
                print(empls,otls,gdt,rdt)
                aast=reass(empls=empls,otls=otls,gdt=gdt,rdt=rdt)
                aast.save()
                sweetify.success(request, title='success', text='add extra accessories Successfully', timer=2000)
                return redirect('index')
            else:
                sweetify.error(request, title='error', text=f'Given Date and Return Data Has Same ({gdt}=={rdt})', timer=3000)
        return render(request, 'addass.html', {'user': u, 'pos': pos,'oth':oth,'em':p.empls})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})




def viewfulldetails(request,id):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        print(id)
        ass=Assest.objects.get(id=id)
        print(ass.systy,ass.empls)
        c=Returncom.objects.all().filter(empname=ass.empls)
        cl=returnlap.objects.all().filter(empname=ass.empls)
        return render(request, 'viewfullcom.html', {'user': u, 'pos': pos,'com':c,'lap':cl})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})




def returnempother(request,id):
    print(id)
    c=reass.objects.get(id=id)
    oth = retOtheracc.objects.all().filter(empname=c.empls)
    print(oth)
    for i in oth:
        if i.keyboard:
            k=Otheracc(keyboard=i.keyboard)
            k.save()
            sweetify.success(request, title='Return', text=f'{i.keyboard} Accessories has Return Successfully')
        elif i.mouse:
            m=Otheracc(mouse=i.mouse)
            m.save()
            sweetify.success(request, title='Return', text=f'{i.mouse} Accessories has Return Successfully')
        elif i.other:
            o=Otheracc(other=i.other)
            o.save()
            sweetify.success(request, title='Return', text=f'{i.other} Accessories has Return Successfully')
        ot=retOtheracc.objects.get(empname=c.empls)
        ot.delete()
        c.delete()
    return redirect('index')

def returnprocess(request,id):
    print(id)
    c=Assest.objects.get(id=id)
    com=Returncom.objects.all().filter(comname=c.systy)
    lap = returnlap.objects.all().filter(lapname=c.systy)
    if com:
        for i in com:
            f = Com(comname=i.comname, os=i.os, hdd=i.hdd, ram=i.ram, cpnm=i.cpnm, cpsn=i.cpsn, monname=i.monname,
                    mnsn=i.mnsn,
                    prcl=i.prcl, grcname=i.grcname, gcs=i.gcs, kyname=i.kyname, msname=i.msname)
            f.save()
            sweetify.success(request, title='Return', text=f'{i.comname} Computer has Return Successfully')
        d = Returncom.objects.get(empname=c.empls)
        d.delete()
        c.delete()
        return redirect('index')
    elif lap:
        for i in lap:
            l = Lap(lapname=i.lapname, los=i.los, lhdd=i.lhdd, lram=i.lram, lcm=i.lcm, lsn=i.lsn, prcl=i.prcl,
                    grcname=i.grcname,
                    gcs=i.gcs, canv=i.canv)
            l.save()
            sweetify.success(request, title='Return', text=f'{i.lapname} laptop has Return Successfully')
        d = returnlap.objects.get(empname=c.empls)
        d.delete()
        c.delete()
        return redirect('index')

def deleteemp(request,id):
    r=Employee.objects.get(id=id)
    r.delete()
    sweetify.success(request, title='Delete', text=f'Deleted Successfully')
    return redirect('index')

def deletecom(request,id):
    c=Com.objects.get(id=id)
    c.delete()
    sweetify.success(request, title='Delete', text=f'Deleted Successfully')
    return redirect('index')
def deletelap(request,id):
    l=Lap.objects.get(id=id)
    l.delete()
    sweetify.success(request, title='Delete', text=f'Deleted Successfully')
    return redirect('index')
def deleteother(request,id):
    o=Otheracc.objects.get(id=id)
    o.delete()
    sweetify.success(request, title='Delete', text=f'Deleted Successfully')
    return redirect('index')

def updateprofile(request):
    try:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        return render(request, 'updateprof.html', {'user': u, 'pos': pos})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})