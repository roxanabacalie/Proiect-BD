from flask import Flask, render_template, jsonify, request, redirect
import cx_Oracle
from datetime import datetime

app = Flask(__name__)
with open(app.root_path + '\config.cfg', 'r') as f:
    app.config['ORACLE_URI'] = f.readline()

con = cx_Oracle.connect("bd065", "parolabd", "bd-dc.cs.tuiasi.ro:1539/orcl")

# volunteers begin code
@app.route('/')
@app.route('/volunteers')
def vol():
    volunteers = []

    cur = con.cursor()
    cur.execute('select * from volunteer')

    for result in cur:
        volunteer = {}
        volunteer['volunteer_id'] = result[0]
        volunteer['last_name'] = result[1]
        volunteer['first_name'] = result[2]
        volunteer['faculty'] = result[3]
        volunteer['email'] = result[4]
        volunteer['phone_number'] = result[5]
        volunteer['city'] = result[6]
        volunteer['department_id'] = result[7]
        volunteers.append(volunteer)
    cur.close()
    return render_template('volunteers.html', volunteers=volunteers)

# -----------------
@app.route('/addVolunteer', methods=['GET', 'POST'])
def add_vol():
    error = None
    if request.method == 'POST':
        dep_name = {}
        name = "'" + request.form['department_name'] + "'"
        vol = 0
        cur = con.cursor()
        cur.execute('select department_id from department where department_name=' + name)
        for result in cur:
            dep_name['department_id'] = result[0]
        cur.close()
        cur = con.cursor()
        cur.execute('select max(volunteer_id) from volunteer')
        for result in cur:
            vol = result[0]
        cur.close()
        vol += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(vol) + "'")
        values.append("'" + request.form['last_name'] + "'")
        values.append("'" + request.form['first_name'] + "'")
        values.append("'" + request.form['faculty'] + "'")
        values.append("'" + request.form['email'] + "'")
        values.append("'" + request.form['phone_number'] + "'")
        values.append("'" + request.form['city'] + "'")
        values.append("'" + str(dep_name['department_id']) + "'")

        fields = ['volunteer_id', 'last_name', 'first_name', 'faculty', 'email', 'phone_number', 'city', 'department_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('volunteer', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/volunteers')

    else:
        dep = []
        cur = con.cursor()
        cur.execute('select department_name from department')
        for result in cur:
            dep.append(result[0])
        cur.close()

        return render_template('addVolunteer.html', department=dep)


@app.route('/delVolunteer', methods=['POST'])
def del_vol():
    vol = request.form['volunteer_id']
    cur = con.cursor()
    cur.execute('delete from volunteer where volunteer_id=' + vol)
    cur.execute('commit')
    return redirect('/volunteers')


@app.route('/editVolunteer', methods=['POST'])
def edit_vol():
    vol = 0
    dep = 0

    cur = con.cursor()
    last_name = request.form['last_name']
    first_name = request.form['first_name']
    cur.execute('select volunteer_id from volunteer where last_name=' + "'" + last_name + "'" +'and first_name= '+ "'" + first_name + "'")
    for result in cur:
        vol = result[0]
    cur.close()

    cur = con.cursor()
    cur.execute('select volunteer_id from appointment where volunteer_id=' + str(vol))
    for result in cur:
        voluntar = result[0]
    cur.close()

    cur = con.cursor()
    cur.execute('select department_id from volunteer where volunteer_id=' + str(vol))
    for result in cur:
        depVechi = result[0]
    cur.close()

    faculty = request.form['faculty']
    email = request.form['email']
    phone_number = request.form['phone_number']
    city = request.form['city']
    department_name = "'" + request.form['department_name'] + "'"
    cur = con.cursor()
    cur.execute('select department_id from department where department_name=' + department_name)
    for result in cur:
        dep = result[0]
    cur.close()
    cur = con.cursor()
    query = """UPDATE volunteer SET last_name=:ln, first_name=:fn, faculty=:f, email=:em, phone_number=:pn, city=:c, department_id=:d where volunteer_id=:v"""
    print(voluntar)
    if (voluntar == vol and dep==depVechi) or (voluntar!=vol):
        cur.execute(query, [last_name, first_name, faculty, email, phone_number, city, dep, vol])
        cur.execute('commit')
    return redirect('/volunteers')


@app.route('/getVolunteer', methods=['POST'])
def get_vol():
    vol = request.form['volunteer_id']
    cur = con.cursor()
    cur.execute('select * from volunteer where volunteer_id=' + "'" + vol + "'")

    vols = cur.fetchone()
    volunteer_id = vols[0]
    last_name = vols[1]
    first_name = vols[2]
    faculty = vols[3]
    email = vols[4]
    phone_number = vols[5]
    city = vols[6]
    department_id = vols[7]
    cur.close()
    department_name = ''
    cur = con.cursor()
    cur.execute('select department_name from department where department_id=' + str(department_id))
    for result in cur:
        department_name = result[0]
    cur.close()

    dep = []
    cur = con.cursor()
    cur.execute('select department_name from department')
    for result in cur:
        dep.append(result[0])
    cur.close()

    return render_template('editVolunteer.html', department=dep, department_name=department_name, last_name=last_name,
                           first_name=first_name, faculty=faculty, email=email, phone_number=phone_number,
                           city=city)

# volunteers end code


# -----------------------------------------#


# departments start code
@app.route('/departments')
def dep():
    departments = []

    cur = con.cursor()
    cur.execute('select * from department')
    for result in cur:
        department = {}
        department['department_id'] = result[0]
        department['department_name'] = result[1]

        departments.append(department)
    cur.close()
    vol = []
    cur = con.cursor()
    cur.execute('select volunteer_id from volunteer')
    # import pdb;pdb.set_trace()
    for result in cur:
        vol.append(result[0])
    cur.close()

    loc = []
    cur = con.cursor()
    cur.execute('select city from location')
    # import pdb;pdb.set_trace()
    for result in cur:
        loc.append(result[0])
    cur.close()
    return render_template('departments.html', departments=departments, volunteers=vol, locations=loc)


# -----------------
@app.route('/addDepartment', methods=['GET', 'POST'])
def add_dep():
    error = None
    if request.method == 'POST':
        dep = 0
        cur = con.cursor()
        cur.execute('select max(department_id) from department')
        for result in cur:
            dep = result[0]
        cur.close()
        dep += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(dep) + "'")
        values.append("'" + request.form['department_name'] + "'")

        fields = ['department_id', 'department_name']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('department', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/departments')

    else:
        dep = []
        cur = con.cursor()
        cur.execute('select department_name from department')
        for result in cur:
            dep.append(result[0])
        cur.close()

        return render_template('addDepartment.html', department=dep)



@app.route('/delDepartment', methods=['POST'])
def del_dep():
    dep = request.form['department_id']
    cur = con.cursor()
    cur.execute('delete from department where department_id=' + dep)
    cur.execute('commit')
    return redirect('/departments')

@app.route('/editDepartment', methods=['POST'])
def edit_dep():
    dep = 0
    cur = con.cursor()

    prev_name = request.form['prev_name']
    next_name = request.form['next_name']
    cur.execute('select department_id from department where department_name=' + "'" + prev_name + "'")
    for result in cur:
        dep = result[0]
    cur.close()


    cur = con.cursor()
    query = """UPDATE department SET department_name=:dn where department_id=:d"""
    cur.execute(query, [next_name, dep])
    cur.execute('commit')
    return redirect('/departments')


@app.route('/getDepartment', methods=['POST'])
def get_dep():
    dep = request.form['department_id']
    cur = con.cursor()
    cur.execute('select * from department where department_id=' + "'" + dep + "'")

    vols = cur.fetchone()
    department_id = vols[0]
    department_name = vols[1]
    cur.close()

    return render_template('editDepartment.html', department_id=department_id, department_name=department_name)


# departments end code
# ------------------------------------------#


# events begin code
@app.route('/')
@app.route('/events')
def ev():
    events = []

    cur = con.cursor()
    cur.execute('select * from event')

    for result in cur:
        event = {}
        event['event_id'] = result[0]
        event['starttime'] = result[1]
        event['endtime'] = result[2]
        event['location_id'] = result[3]

        events.append(event)
    cur.close()
    return render_template('events.html', events=events)

# -----------------
@app.route('/addEvent', methods=['GET', 'POST'])
def add_ev():
    error = None
    if request.method == 'POST':

        cur = con.cursor()
        cur.execute('select max(event_id) from event')
        for result in cur:
            eve = result[0]
        cur.close()
        eve += 1
        cur = con.cursor()
        values = []
        values.append( str(eve) )
        values.append("to_timestamp(" + "substr(" + "'"+request.form['starttime'] + "', 1, 10)" + "||" + "substr(" + "'"+request.form['starttime'] + "', 12, 8)"+", " + "'YYYY-MM-DD HH24:MI:SS')")
        values.append("to_timestamp(" + "substr(" + "'"+request.form['endtime'] + "', 1, 10)" + "||" + "substr(" + "'"+request.form['endtime'] + "', 12, 8)"+", " + "'YYYY-MM-DD HH24:MI:SS')")
        values.append( request.form['location_id'])
        print(request.form['starttime'])
        fields = ['event_id', 'starttime', 'endtime', 'location_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('event', ', '.join(fields), ', '.join(values))
        print(query)
        cur.execute(query)
        cur.execute('commit')
        return redirect('/events')

    else:
        locat = []
        cur = con.cursor()
        cur.execute('select location_id from location')
        for result in cur:
            locat.append(result[0])
        cur.close()

        return render_template('addEvent.html', location=locat)


@app.route('/delEvent', methods=['POST'])
def del_ev():
    ev = request.form['event_id']
    cur = con.cursor()
    cur.execute('delete from event where event_id=' + ev)
    cur.execute('commit')
    return redirect('/events')


@app.route('/editEvent', methods=['POST'])
def edit_ev():

    event_id = request.form['event_id']
    starttime="to_timestamp(" + "substr(" + "'"+request.form['starttime'] + "', 1, 10)" + "||" + "substr(" + "'"+request.form['starttime'] + "', 12, 8)"+", " + "'YYYY-MM-DD HH24:MI:SS')"
    endtime="to_timestamp(" + "substr(" + "'"+request.form['endtime'] + "', 1, 10)" + "||" + "substr(" + "'"+request.form['endtime'] + "', 12, 8)"+", " + "'YYYY-MM-DD HH24:MI:SS')"
    location_id = request.form['location_id']
    print(starttime)
    print(location_id)
    print(event_id)

    cur = con.cursor()
    fields1 = [starttime]
    fields2=[endtime]
    fields3=[location_id]
    fields4=[event_id]
    query = 'UPDATE %s SET starttime=%s, endtime=%s, location_id=%s where event_id=%s' % ('event', ', '.join(fields1), ', '.join(fields2), ', '.join(fields3), ', '.join(fields4))
    print(query)
    cur.execute(query)
    cur.execute('commit')



   #cur = con.cursor()
    #query = """UPDATE event SET starttime=:st, endtime=:et, location_id=:l where event_id=:v"""

    #cur.execute(query, [starttime, endtime, location_id, event_id])
    #print(query)
    #cur.execute('commit')
    return redirect('/events')
    return redirect('/events')


@app.route('/getEvent', methods=['POST'])
def get_ev():
    event=[]
    ev = request.form['event_id']
    cur = con.cursor()
    cur.execute('select event_id from event where event_id=' + "'" + ev + "'")
    for result in cur:
        event.append(result[0])
    cur.close()

    location = []
    cur = con.cursor()
    cur.execute('select location_id from location')
    for result in cur:
        location.append(result[0])
    cur.close()

    return render_template('editEvent.html', event=event, location=location)
# events end code





# locations begin code
@app.route('/')
@app.route('/locations')
def loc():
    locations = []

    cur = con.cursor()
    cur.execute('select * from location')

    for result in cur:
        location = {}
        location['location_id'] = result[0]
        location['city'] = result[1]
        location['county'] = result[2]
        location['street'] = result[3]
        location['number_of_street'] = result[4]

        locations.append(location)
    cur.close()
    return render_template('locations.html', locations=locations)

# -----------------

@app.route('/addLocation', methods=['GET', 'POST'])
def add_loc():
    error = None
    if request.method == 'POST':

        cur = con.cursor()
        cur.execute('select max(location_id) from location')
        for result in cur:
            locat = result[0]
        cur.close()
        locat += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(locat) + "'")
        values.append("'" + request.form['city'] + "'")
        values.append("'" + request.form['county'] + "'")
        values.append("'" + request.form['street'] + "'")
        values.append("'" + request.form['number_of_street'] + "'")

        fields = ['location_id', 'city', 'county', 'street', 'number_of_street']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('location', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/locations')

    else:
        dep = []
        cur = con.cursor()
        cur.execute('select department_name from department')
        for result in cur:
            dep.append(result[0])
        cur.close()

        return render_template('addLocation.html', department=dep)


@app.route('/delLocation', methods=['POST'])
def del_loc():
    vol = request.form['location_id']
    cur = con.cursor()
    cur.execute('delete from location where location_id=' + vol)
    cur.execute('commit')
    return redirect('/locations')


@app.route('/editLocation', methods=['POST'])
def edit_loc():

    location_id = request.form['location_id']
    city = request.form['city']
    county = request.form['county']
    street = request.form['street']
    number_of_street = request.form['number_of_street']


    cur = con.cursor()
    fields1 = ["'"+city+"'"]
    fields2 = ["'"+county+"'"]
    fields3 = ["'"+street+"'"]
    fields4 = [number_of_street]
    fields5=[location_id]
    query = 'UPDATE %s SET city=%s, county=%s, street=%s, number_of_street=%s where location_id=%s' % ('location', ', '.join(fields1), ', '.join(fields2), ', '.join(fields3), ', '.join(fields4), ', '.join(fields5))
    print(query)
    cur.execute(query)
    cur.execute('commit')

    return redirect('/locations')

@app.route('/getLocation', methods=['POST'])
def get_loc():

    locat = []
    lid=request.form['location_id']
    cur = con.cursor()
    cur.execute('select location_id from location where location_id=' + "'" + lid + "'")
    for result in cur:
        locat.append(result[0])
    cur.close()


    return render_template('editLocation.html', locations=locat)

# locations end code


# requirements begin code
@app.route('/')
@app.route('/requirements')
def req():
    requirements = []

    cur = con.cursor()
    cur.execute('select * from requirement')

    for result in cur:
        requirement = {}
        requirement['requirement_id'] = result[0]
        requirement['number_of_volunteers'] = result[1]
        requirement['event_id'] = result[2]
        requirement['department_id'] = result[3]
        requirements.append(requirement)
    cur.close()
    return render_template('requirements.html', requirements=requirements)

# -----------------
@app.route('/addRequirement', methods=['GET', 'POST'])
def add_req():
    error = None
    if request.method == 'POST':

        dep_name = {}
        name = "'" + request.form['department_name'] + "'"

        req = 0
        cur = con.cursor()
        cur.execute('select department_id from department where department_name=' + name)
        for result in cur:
            dep_name['department_id'] = result[0]
        cur.close()

        cur = con.cursor()
        cur.execute('select max(requirement_id) from requirement')
        for result in cur:
            req = result[0]
        cur.close()
        req += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(req) + "'")
        values.append("'" + request.form['number_of_volunteers'] + "'")
        values.append("'" + request.form['event_id'] + "'")
        values.append("'" + str(dep_name['department_id']) + "'")

        fields = ['requirement_id', 'number_of_volunteers', 'event_id', 'department_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('requirement', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/requirements')

    else:
        dep = []
        cur = con.cursor()
        cur.execute('select department_name from department')
        for result in cur:
            dep.append(result[0])
        cur.close()

        eve=[]
        cur=con.cursor()
        cur.execute('select event_id from event')
        for result in cur:
            eve.append(result[0])
        cur.close()

        return render_template('addRequirement.html', department=dep, event=eve)


@app.route('/delRequirement', methods=['POST'])
def del_req():
    vol = request.form['requirement_id']
    cur = con.cursor()
    cur.execute('delete from requirement where requirement_id=' + vol)
    cur.execute('commit')
    return redirect('/requirements')


@app.route('/editRequirement', methods=['POST'])
def edit_req():

    requirement_id = request.form['requirement_id']
    number_of_volunteers = request.form['number_of_volunteers']


    cur = con.cursor()
    cur.execute('select count(appointment_id) from appointment where requirement_id=' + requirement_id)
    for result in cur:
        nrProgramati = result[0]
    cur.close()

    cur = con.cursor()
    fields1 = [number_of_volunteers]
    fields2 = [requirement_id]

    if int(number_of_volunteers)>=nrProgramati:
        query = 'UPDATE %s SET number_of_volunteers=%s where requirement_id=%s' % ('requirement', ', '.join(fields1), ', '.join(fields2))
        cur.execute(query)
        cur.execute('commit')

    return redirect('/requirements')

@app.route('/getRequirement', methods=['POST'])
def get_req():

    re = []
    rid=request.form['requirement_id']
    cur = con.cursor()
    print(rid)
    cur.execute('select requirement_id from requirement where requirement_id=' + "'" + rid + "'")
    for result in cur:
        re.append(result[0])
    cur.close()

    eve = []
    cur = con.cursor()
    cur.execute('select event_id from event')
    for result in cur:
        eve.append(result[0])
    cur.close()


    dep = []
    cur = con.cursor()
    cur.execute('select department_id from department')
    for result in cur:
        dep.append(result[0])
    cur.close()

    return render_template('editRequirement.html', requirements=re, events=eve, departments=dep)

# requirements end code



# appointments begin code
@app.route('/')
@app.route('/appointments')
def appo():
    appointments = []

    cur = con.cursor()
    cur.execute('select * from appointment')

    for result in cur:
        appointment = {}
        appointment['appointment_id'] = result[0]
        appointment['attendance'] = result[1]
        appointment['volunteer_id'] = result[2]
        appointment['requirement_id'] = result[3]
        appointments.append(appointment)
    cur.close()
    return render_template('appointments.html', appointments=appointments)

# -----------------

@app.route('/addAppointment', methods=['GET', 'POST'])
def add_app():
    error = None
    if request.method == 'POST':
        req = 0
        cur = con.cursor()
        cur.execute('select max(appointment_id) from appointment')
        for result in cur:
            req = int(result[0])
        cur.close()
        req += 1

        cur = con.cursor()
        cur.execute('select count(appointment_id) from appointment where requirement_id='+request.form['requirement_id'])
        for result in cur:
            nrProgramati = result[0]
        cur.close()

        cur = con.cursor()
        cur.execute('select number_of_volunteers from requirement where requirement_id='+request.form['requirement_id'])
        for result in cur:
            nrNecesari = result[0]
        cur.close()

        cur = con.cursor()
        cur.execute('select department_id from volunteer where volunteer_id=' + request.form['volunteer_id'])
        for result in cur:
            deptReal = result[0]
        cur.close()

        cur = con.cursor()
        cur.execute('select department_id from requirement where requirement_id=' + request.form['requirement_id'])
        for result in cur:
            deptDorit = result[0]
        cur.close()

        cur = con.cursor()
        values = []
        values.append("'" + str(req) + "'")
        values.append("'" + request.form['volunteer_id'] + "'")
        values.append("'" + request.form['requirement_id'] + "'")

        fields = ['appointment_id', 'volunteer_id', 'requirement_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('appointment', ', '.join(fields), ', '.join(values))

        if nrProgramati<nrNecesari:
            if deptReal==deptDorit:
                cur.execute(query)
                cur.execute('commit')
            else:
                print("departament gresit")
        else:
            print("depasire")
        return redirect('/appointments')

    else:
        dep = []
        cur = con.cursor()
        cur.execute('select department_name from department')
        for result in cur:
            dep.append(result[0])
        cur.close()

        eve = []
        cur = con.cursor()
        cur.execute('select volunteer_id from volunteer')
        for result in cur:
            eve.append(result[0])
        cur.close()

        return render_template('addAppointment.html', department=dep, volunteers=eve)
    """
    error = None
    if request.method == 'POST':

        cur = con.cursor()
        cur.execute('select max(appointment_id) from appointment')
        for result in cur:
            appo = result[0]
        cur.close()
        appo += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(appo) + "'")
        values.append("'" + request.form['volunteer_id'] + "'")
        values.append("'" + request.form['requirement_id'] + "'")

        fields = ['appointment_id', 'volunteer_id', 'requirement_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('appointment', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/appointments')

    else:
        vol = []
        cur = con.cursor()
        cur.execute('select v.volunteer_id from volunteer v, requirement r where v.department_id=r.department_id and r.requirement_id='+ request.form['requirement_id'])
        for result in cur:
            vol.append(result[0])
        cur.close()

        return render_template('addAppointment.html', volunteers=vol)

"""
@app.route('/delAppointment', methods=['POST'])
def del_app():
    vol = request.form['appointment_id']
    cur = con.cursor()
    cur.execute('delete from appointment where appointment_id=' + vol)
    cur.execute('commit')
    return redirect('/appointments')


@app.route('/editAppointment', methods=['POST'])
def edit_app():

    appointment_id = request.form['appointment_id']
    attendance = request.form['attendance']
    volunteer_id = request.form['volunteer_id']
    requirement_id = request.form['requirement_id']

    cur = con.cursor()
    cur.execute('select requirement_id from appointment where appointment_id=' + "'" + appointment_id + "'")
    for result in cur:
        old_requirement_id=result[0];
    cur.close()

    cur = con.cursor()
    cur.execute('select count(appointment_id) from appointment where requirement_id=' + str(requirement_id))
    for result in cur:
        nrProgramati = result[0]
        print(nrProgramati)
    cur.close()

    cur = con.cursor()
    cur.execute('select number_of_volunteers from requirement where requirement_id=' + str(requirement_id))
    for result in cur:
        nrNecesari = result[0]
        print(nrNecesari)
    cur.close()

    cur = con.cursor()
    cur.execute('select department_id from requirement where requirement_id=' + str(requirement_id))
    for result in cur:
        depNou = result[0]
        print(depNou)
    cur.close()

    cur = con.cursor()
    cur.execute('select department_id from requirement where requirement_id=' + str(old_requirement_id))
    for result in cur:
        depVechi = result[0]
        print(depVechi)
    cur.close()



    cur = con.cursor()
    fields1 = ["'"+attendance+"'"]
    fields2 = [volunteer_id]
    fields3 = [requirement_id]
    fields4 = [appointment_id]

    query = 'UPDATE %s SET attendance=%s, volunteer_id=%s, requirement_id=%s where appointment_id=%s' % ('appointment', ', '.join(fields1), ', '.join(fields2), ', '.join(fields3), ', '.join(fields4))
    print(query)
    if (old_requirement_id==requirement_id) or ((old_requirement_id!=requirement_id) and (nrNecesari>nrProgramati) and (depNou==depVechi)):
        cur.execute(query)
        cur.execute('commit')

    return redirect('/appointments')

@app.route('/getAppointment', methods=['POST'])
def get_app():

    locat = []
    lid=request.form['appointment_id']
    cur = con.cursor()
    cur.execute('select appointment_id from appointment where appointment_id=' + "'" + lid + "'")
    for result in cur:
        locat.append(result[0])
    cur.close()

    vol = []
    cur = con.cursor()
    cur.execute('select volunteer_id from volunteer')
    for result in cur:
        vol.append(result[0])
    cur.close()

    req = []
    cur = con.cursor()
    cur.execute('select requirement_id from requirement')
    for result in cur:
        req.append(result[0])
    cur.close()

    return render_template('editAppointment.html', appointments=locat, volunteers=vol, requirements=req)
# appointments end code





# observations begin code
@app.route('/')
@app.route('/observations')
def obs():
    observations = []

    cur = con.cursor()
    cur.execute('select * from observation')

    for result in cur:
        observation = {}
        observation['observation_id'] = result[0]
        observation['message'] = result[1]
        observation['appointment_id'] = result[2]

        observations.append(observation)
    cur.close()
    return render_template('observations.html', observations=observations)

# -----------------
@app.route('/addObservation', methods=['GET', 'POST'])
def add_obs():
    error = None
    if request.method == 'POST':

        cur = con.cursor()
        cur.execute('select max(observation_id) from observation')
        for result in cur:
            vol = result[0]
        cur.close()
        vol += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(vol) + "'")
        values.append("'" + request.form['message'] + "'")
        values.append("'" + request.form['appointment_id'] + "'")

        fields = ['observation_id', 'message', 'appointment_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('observation', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/observations')

    else:
        dep = []
        cur = con.cursor()
        cur.execute('select appointment_id from appointment')
        for result in cur:
            dep.append(result[0])
        cur.close()

        return render_template('addObservation.html', appointments=dep)


@app.route('/delObservation', methods=['POST'])
def del_obs():
    vol = request.form['observation_id']
    cur = con.cursor()
    cur.execute('delete from observation where observation_id=' + vol)
    cur.execute('commit')
    return redirect('/observations')


@app.route('/editObservation', methods=['POST'])
def edit_obs():

    observation_id = request.form['observation_id']
    message = request.form['message']

    cur = con.cursor()
    fields1 = ["'"+message+"'"]
    fields2 = [observation_id]

    query = 'UPDATE %s SET message=%s where observation_id=%s' % ('observation', ', '.join(fields1), ', '.join(fields2))
    cur.execute(query)
    cur.execute('commit')

    return redirect('/observations')

@app.route('/getObservation', methods=['POST'])
def get_obs():

    locat = []
    lid=request.form['observation_id']
    cur = con.cursor()
    cur.execute('select observation_id from observation where observation_id=' + "'" + lid + "'")
    for result in cur:
        locat.append(result[0])
    cur.close()

    vol = []
    cur = con.cursor()
    cur.execute('select volunteer_id from volunteer')
    for result in cur:
        vol.append(result[0])
    cur.close()

    return render_template('editObservation.html', observations=locat)

# observations end code


# main
if __name__ == '__main__':
    app.run(debug=True)
    con.close()


