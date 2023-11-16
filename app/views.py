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
    ass=Assest.objects.all()
    asss=len(ass)
    po = reass.objects.all()
    poo = len(po)
    fass = asss + poo
    asl = []
    coml = []
    retcoml = []
    lapl=[]
    retlapl=[]
    otherl=[]
    retotherl=[]
    mo = chart.objects.all().filter()
    for i in mo:
        if i.assest != None:
            asl.append(i.assest)
        else:
            asl.append(0)
        if i.com != None:
            coml.append(i.com)
        else:
            coml.append(0)
        if i.retcom != None:
            retcoml.append(i.retcom)
        else:
            retcoml.append(0)
        if i.lap != None:
            lapl.append(i.lap)
        else:
            lapl.append(0)
        if i.retlap != None:
            retlapl.append(i.retlap)
        else:
            retlapl.append(0)
        if i.other != None:
            otherl.append(i.other)
        else:
            otherl.append(0)
        if i.retother != None:
            retotherl.append(i.retother)
        else:
            retotherl.append(0)
    to=todolist.objects.all()
    if 'email' in request.session:
        a = Register.objects.get(email=request.session['email'])
        u = a.user
        pos = a.postion
        return render(request, 'index.html', {'user': u, 'emp': p, 'pos': pos, 'com': cl, 'lap': lp,'ass':fass,'asl':asl,'coml': coml,'retcoml': retcoml,'lapl': lapl, 'retlapl': retlapl,'otherl': otherl, 'retotherl': retotherl,'todo':to})
    else:
        return render(request, 'index.html', {'user': None, 'emp': p, 'pos': None, 'com': cl, 'lap': lp,'ass':asss, 'asl':asl,'coml': coml,'retcoml': retcoml,'lapl': lapl, 'retlapl': retlapl,'otherl': otherl, 'retotherl': retotherl})


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
            c=Com.objects.all()
            o=[]
            for i in c:
                o.append(i.comname)
            print(o)
            recom=Returncom.objects.all()
            r=[]
            for j in recom:
                r.append(j.comname)
            if comname not in o:
                if comname not in r:
                    com = Com(comname=comname, os=os, hdd=hdd, ram=ram, cpnm=cpnm, cpsn=cpsn, monname=monname,
                              mnsn=mnsn,
                              prcl=prcl, grcname=grcname, gcs=gcs, kyname=kyname, msname=msname)
                    com.save()
                    asee = Assest.objects.all()
                    asse = len(asee)
                    po = reass.objects.all()
                    poo = len(po)
                    fass = asse + poo
                    cooo = Com.objects.all()
                    coe = len(cooo)
                    recm = Returncom.objects.all()
                    reco = len(recm)
                    lppp = Lap.objects.all()
                    cl = len(lppp)
                    relapp = returnlap.objects.all()
                    relaap = len(relapp)
                    cooo = Otheracc.objects.all()
                    cob = len(cooo)
                    recmmm = retOtheracc.objects.all()
                    recom = len(recmmm)
                    m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
                    m.save()
                    sweetify.success(request, title='success', text=f'{comname} Details Register Successfully',
                                     timer=2000)
                    return redirect('comcat')
                else:
                    sweetify.error(request, title='Error', text=f'That {comname} Name has already got on employee', timer=2000)
                    return redirect('comcat')
            else:
                sweetify.error(request, title='Error', text=f'That { comname } Name has already exists', timer=2000)
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
            c = Lap.objects.all()
            o = []
            for i in c:
                o.append(i.lapname)
            rl=[]
            rlp=returnlap.objects.all()
            for j in rlp:
                rl.append(j.lapname)
            if lapname not in o:
                if lapname not in rl:
                    lap = Lap(lapname=lapname, los=los, lhdd=lhdd, lram=lram, lcm=lcm, lsn=lsn, prcl=prcl,
                              grcname=grcname,
                              gcs=gcs, canv=canv)
                    lap.save()
                    asee = Assest.objects.all()
                    asse = len(asee)
                    po = reass.objects.all()
                    poo = len(po)
                    fass = asse + poo
                    cooo = Com.objects.all()
                    coe = len(cooo)
                    recm = Returncom.objects.all()
                    reco = len(recm)
                    lppp = Lap.objects.all()
                    cl = len(lppp)
                    relapp = returnlap.objects.all()
                    relaap = len(relapp)
                    cooo = Otheracc.objects.all()
                    cob = len(cooo)
                    recmmm = retOtheracc.objects.all()
                    recom = len(recmmm)
                    m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
                    m.save()
                    print('s')
                    sweetify.success(request, title='success', text=f'{lapname} Details Register Successfully',
                                     timer=2000)
                    return redirect('lapcat')
                else:
                    sweetify.error(request, title='Error', text=f'That {lapname} Name has already got on employee', timer=2000)
                    return redirect('lapcat')
            else:
                sweetify.error(request, title='Error', text=f'That { lapname } Name has already exists', timer=2000)
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
            ork=[]
            ortk=retOtheracc.objects.all().filter(keyboard=keyboard)
            for i in ortk:
                ork.append(i.keyboard)
            m=[]
            om=Otheracc.objects.all().filter(mouse=mouse)
            for i in om:
                m.append(i.mouse)
            orm = []
            ortm = retOtheracc.objects.all().filter(mouse=mouse)
            for i in ortm:
                orm.append(i.mouse)
            o=[]
            oo=Otheracc.objects.all().filter(other=other)
            for i in oo:
                o.append(i.other)
            oro = []
            orto = retOtheracc.objects.all().filter(other=other)
            for i in orto:
                oro.append(i.other)
            if keyboard:
                if keyboard not in p:
                    if keyboard not in ork:
                        oth = Otheracc(keyboard=keyboard)
                        oth.save()
                        asee = Assest.objects.all()
                        asse = len(asee)
                        po = reass.objects.all()
                        poo = len(po)
                        fass = asse + poo
                        cooo = Com.objects.all()
                        coe = len(cooo)
                        recm = Returncom.objects.all()
                        reco = len(recm)
                        lppp = Lap.objects.all()
                        cl = len(lppp)
                        relapp = returnlap.objects.all()
                        relaap = len(relapp)
                        cooo = Otheracc.objects.all()
                        cob = len(cooo)
                        recmmm = retOtheracc.objects.all()
                        recom = len(recmmm)
                        m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
                        m.save()
                        sweetify.success(request, title='success', text='Other Accessories Register Successfully',
                                         timer=2000)
                        return redirect('otheracc')
                    else:
                        sweetify.error(request, title='error',
                                       text=f'That {keyboard} has already got on employee please Given Other name')
                        return redirect('otheracc')
                else:
                    sweetify.error(request, title='error', text=f'That {keyboard} has already exists please Given Other name')
                    return redirect('otheracc')
            elif mouse:
                if mouse not in m:
                    if mouse not in orm:
                        oth = Otheracc(mouse=mouse)
                        oth.save()
                        asee = Assest.objects.all()
                        asse = len(asee)
                        po = reass.objects.all()
                        poo = len(po)
                        fass = asse + poo
                        cooo = Com.objects.all()
                        coe = len(cooo)
                        recm = Returncom.objects.all()
                        reco = len(recm)
                        lppp = Lap.objects.all()
                        cl = len(lppp)
                        relapp = returnlap.objects.all()
                        relaap = len(relapp)
                        cooo = Otheracc.objects.all()
                        cob = len(cooo)
                        recmmm = retOtheracc.objects.all()
                        recom = len(recmmm)
                        m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
                        m.save()
                        sweetify.success(request, title='success', text='Other Accessories Register Successfully',
                                         timer=2000)
                        return redirect('otheracc')
                    else:
                        sweetify.error(request, title='error',
                                       text=f'That {mouse} has already got on employee please Given Other name')
                        return redirect('otheracc')

                else:
                    sweetify.error(request, title='error', text=f'That {mouse} has already exists please Given Other name')
                    return redirect('otheracc')
            elif other:
                if other not in o:
                    if other not in oro:
                        oth = Otheracc(other=other)
                        oth.save()
                        asee = Assest.objects.all()
                        asse = len(asee)
                        po = reass.objects.all()
                        poo = len(po)
                        fass = asse + poo
                        cooo = Com.objects.all()
                        coe = len(cooo)
                        recm = Returncom.objects.all()
                        reco = len(recm)
                        lppp = Lap.objects.all()
                        cl = len(lppp)
                        relapp = returnlap.objects.all()
                        relaap = len(relapp)
                        cooo = Otheracc.objects.all()
                        cob = len(cooo)
                        recmmm = retOtheracc.objects.all()
                        recom = len(recmmm)
                        m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
                        m.save()
                        sweetify.success(request, title='success', text=f'{other} Register Successfully',
                                         timer=2000)
                        return redirect('otheracc')
                    else:
                        sweetify.error(request, title='error',
                                       text=f'That {other} has already got on employee please Given Other name')
                        return redirect('otheracc')
                else:
                    sweetify.error(request, title='error', text=f'That {other} has already exists please Given Other name')
                    return redirect('otheracc')
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
            if gdt != rdt:
                fgdt = gdt[8:]
                frdt = rdt[8:]
                if fgdt < frdt:
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
                                ooo.delete()
                                oo = retOtheracc(empname=empls, other=otls)
                                oo.save()
                                break
                        aast=reass(empls=empls,otls=otls,gdt=gdt,rdt=rdt)
                        aast.save()
                        asee = Assest.objects.all()
                        asse = len(asee)
                        po = reass.objects.all()
                        poo = len(po)
                        fass = asse + poo
                        cooo = Com.objects.all()
                        coe = len(cooo)
                        recm = Returncom.objects.all()
                        reco = len(recm)
                        lppp = Lap.objects.all()
                        cl = len(lppp)
                        relapp = returnlap.objects.all()
                        relaap = len(relapp)
                        cooo = Otheracc.objects.all()
                        cob = len(cooo)
                        recmmm = retOtheracc.objects.all()
                        recom = len(recmmm)
                        m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
                        m.save()
                        sweetify.success(request, title='success', text='add Other accessories Successfully', timer=2000)
                        return redirect('index')
                else:
                    sweetify.error(request, title='error', text=f'Return Date should be after the given date ({gdt}>{rdt})',timer=3000)
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
            if gdt != rdt:
                fgdt=gdt[8:]
                frdt=rdt[8:]
                if fgdt < frdt:
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
                                dt=Returncom(empname=empls,comname=i.comname,os=i.os, hdd=i.hdd, ram=i.ram, cpnm=i.cpnm, cpsn=i.cpsn,
                                           monname=i.monname, mnsn=i.mnsn, prcl=i.prcl, grcname=i.grcname, gcs=i.gcs,
                                           kyname=i.kyname, msname=i.msname)
                                dt.save()
                                cmm=Com.objects.get(comname=cmpls)
                                cmm.delete()
                    if lpls != 'None':
                        if empls in rlp or empls in rec:
                            sweetify.error(request,title='error',text=f'{empls} already got the Computer or laptop',timer=3000)
                            return redirect('/')
                        else:
                            systy=lpls
                            lps=Lap.objects.all().filter(lapname=lpls)
                            for i in lps:
                                dl=returnlap(empname=empls,lapname=i.lapname, los=i.los, lhdd=i.lhdd, lram=i.lram, lcm=i.lcm, lsn=i.lsn,
                                           prcl=i.prcl, grcname=i.grcname, gcs=i.gcs, canv=i.canv)
                                dl.save()
                                lpp=Lap.objects.get(lapname=lpls)
                                lpp.delete()
                    aast=Assest(empls=empls,systy=systy,gdt=gdt,rdt=rdt)
                    aast.save()
                    asee = Assest.objects.all()
                    asse = len(asee)
                    po = reass.objects.all()
                    poo = len(po)
                    fass = asse + poo
                    cooo = Com.objects.all()
                    coe = len(cooo)
                    recm = Returncom.objects.all()
                    reco = len(recm)
                    lppp = Lap.objects.all()
                    cl = len(lppp)
                    relapp = returnlap.objects.all()
                    relaap = len(relapp)
                    cooo = Otheracc.objects.all()
                    cob = len(cooo)
                    recmmm = retOtheracc.objects.all()
                    recom = len(recmmm)
                    m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
                    m.save()
                    sweetify.success(request, title='success', text='Assest Register Successfully', timer=2000)
                    return redirect('viewass')
                else:
                    sweetify.error(request, title='error', text=f'Return Date should be after the given date ({gdt}>{rdt})',timer=3000)
            else:
                sweetify.error(request, title='error', text=f'Given Date and Return Date Has Same ({gdt}=={rdt})', timer=3000)

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
            if gdt != rdt:
                fgdt = gdt[8:]
                frdt = rdt[8:]
                if fgdt < frdt:
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
                                ooo.delete()
                                oo = retOtheracc(empname=empls, other=otls)
                                oo.save()
                                break
                        aast=reass(empls=empls,otls=otls,gdt=gdt,rdt=rdt)
                        aast.save()
                        asee = Assest.objects.all()
                        asse = len(asee)
                        po = reass.objects.all()
                        poo = len(po)
                        fass = asse + poo
                        cooo = Com.objects.all()
                        coe = len(cooo)
                        recm = Returncom.objects.all()
                        reco = len(recm)
                        lppp = Lap.objects.all()
                        cl = len(lppp)
                        relapp = returnlap.objects.all()
                        relaap = len(relapp)
                        cooo = Otheracc.objects.all()
                        cob = len(cooo)
                        recmmm = retOtheracc.objects.all()
                        recom = len(recmmm)
                        m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
                        m.save()
                        sweetify.success(request, title='success', text='add extra accessories Successfully', timer=2000)
                        return redirect('index')
                else:
                    sweetify.error(request, title='error', text=f'Return Date should be after the given date ({gdt}>{rdt})',timer=3000)
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
        ass=Assest.objects.get(id=id)
        c=Returncom.objects.all().filter(empname=ass.empls)
        cl=returnlap.objects.all().filter(empname=ass.empls)
        return render(request, 'viewfullcom.html', {'user': u, 'pos': pos,'com':c,'lap':cl})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})




def returnempother(request,id):
    print(id)
    c=reass.objects.get(id=id)
    # print(c)
    # print(c.empls,c.otls)
    reto=retOtheracc.objects.filter(empname=c.empls)
    # print(reto)
    for i in reto:
        if i.keyboard == c.otls:
            k = Otheracc(keyboard=i.keyboard)
            k.save()
            reoter = retOtheracc.objects.get(keyboard=i.keyboard)
            reoter.delete()
            c.delete()
            sweetify.success(request, title='Return', text=f'{i.keyboard} Accessories has Return Successfully')
        elif i.mouse == c.otls:
            m = Otheracc(mouse=i.mouse)
            m.save()
            reoter = retOtheracc.objects.get(mouse=i.mouse)
            reoter.delete()
            c.delete()
            sweetify.success(request, title='Return', text=f'{i.mouse} Accessories has Return Successfully')
        elif i.other == c.otls:
            o = Otheracc(other=i.other)
            o.save()
            reoter = retOtheracc.objects.get(other=i.other)
            reoter.delete()
            c.delete()
            sweetify.success(request, title='Return', text=f'{i.other} Accessories has Return Successfully')
    asee = Assest.objects.all()
    asse = len(asee)
    po = reass.objects.all()
    poo = len(po)
    fass = asse + poo
    cooo = Com.objects.all()
    coe = len(cooo)
    recm = Returncom.objects.all()
    reco = len(recm)
    lppp = Lap.objects.all()
    cl = len(lppp)
    relapp = returnlap.objects.all()
    relaap = len(relapp)
    cooo = Otheracc.objects.all()
    cob = len(cooo)
    recmmm = retOtheracc.objects.all()
    recom = len(recmmm)
    m = chart(assest=fass,com=coe,retcom=reco,lap=cl,retlap=relaap,other=cob, retother=recom)
    m.save()
    return redirect('index')

def returnprocess(request,id):
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
        asee = Assest.objects.all()
        asse = len(asee)
        po = reass.objects.all()
        poo = len(po)
        fass = asse + poo
        cooo = Com.objects.all()
        coe = len(cooo)
        recm = Returncom.objects.all()
        reco = len(recm)
        lppp = Lap.objects.all()
        cl = len(lppp)
        relapp = returnlap.objects.all()
        relaap = len(relapp)
        cooo = Otheracc.objects.all()
        cob = len(cooo)
        recmmm = retOtheracc.objects.all()
        recom = len(recmmm)
        m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
        m.save()
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
        asee = Assest.objects.all()
        asse = len(asee)
        po = reass.objects.all()
        poo = len(po)
        fass = asse + poo
        cooo = Com.objects.all()
        coe = len(cooo)
        recm = Returncom.objects.all()
        reco = len(recm)
        lppp = Lap.objects.all()
        cl = len(lppp)
        relapp = returnlap.objects.all()
        relaap = len(relapp)
        cooo = Otheracc.objects.all()
        cob = len(cooo)
        recmmm = retOtheracc.objects.all()
        recom = len(recmmm)
        m = chart(assest=fass, com=coe, retcom=reco, lap=cl, retlap=relaap, other=cob, retother=recom)
        m.save()
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
        b=Register.objects.all().filter(email=request.session['email'])
        return render(request, 'updateprof.html', {'user': u, 'pos': pos,'pro':b})
    except:
        return render(request, 'signrequestpage.html', {'user': None, 'pos': None})

def actionupdate(request,id):
    if request.method == "POST":
        user = request.POST.get('user')
        mobno = request.POST.get('mobno')
        postion = request.POST.get('postion')
        staffid = request.POST.get('staffid')
        a=Register.objects.get(id=id)
        a.user=user
        a.mobno=mobno
        a.postion=postion
        a.staffid=staffid
        a.save()
        sweetify.success(request, title='Update', text=f'Updated Successfully')
    return redirect('index')

def todolis(request):
    if 'email' in request.session:
        if request.method == 'POST':
            task = request.POST.get('task')
            print(task)
            tl=[]
            to=todolist.objects.all()
            for i in to:
                tl.append(i.todo)
            if task not in tl:
                t = todolist(todo=task)
                t.save()
                sweetify.success(request, title='Todo', text=f'Todolist addedd Successfully')
                return redirect('index')
            else:
                sweetify.error(request, title='Todo Error', text=f'Todolist Already Exists')
                return redirect('index')
    else:
        sweetify.error(request,title='Sign request',text='Please Login The Page')
        return redirect('index')

def tododel(request,id):
    t=todolist.objects.get(id=id)
    t.delete()
    sweetify.success(request, title='Delete', text=f'Deleted Successfully')
    return redirect('index')
