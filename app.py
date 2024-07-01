from flask import Flask, render_template, jsonify, request,Response, Request
from database import loaddb,load_job_from_db, add_application_to_db


app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html", jobs=loaddb(), Company="Parayil"  )

@app.route("/mission")
def mission():
    return render_template("mission.html",  Company="Parayil"  )

@app.route("/api/jobs")
def list_jobs():
    jobs=loaddb()
    return jsonify(jobs)



@app.route("/jobs/<job_id>")
def showjob_detail(job_id):
  jobsbyid=load_job_from_db(job_id)
  
  return  render_template("jobpagedetail.html", jobsbyid=load_job_from_db(job_id),  Company="Parayil"  )



@app.route("/jobs/apply/<job_id>", methods=['post']) 
def applicationform(job_id ):
  data= request.form
  job=load_job_from_db(job_id)
  add_application_to_db(job_id, data)
  return render_template('application_submitted.html', 
     data=data,
     job=job)


@app.route("/jobs/api/<id>")
def showjobapi_detail(job_id):
  jobsbyid=load_job_from_db(job_id)
  return jsonify(job)  

if __name__=="__main__":
  print("i am inside you")
  app.run(host='0.0.0.0', debug=True)