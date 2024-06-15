from flask import Flask, render_template, jsonify,request,redirect 
from database import loaddb,load_job_from_db



app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html", jobs=loaddb(), Company="Parayil"  )



@app.route("/api/jobs")
def list_jobs():
    jobs=loaddb()
    return jsonify(jobs)



@app.route("/jobpagedetail.html/<id>")
def showjob_detail(id):
  job=load_job_from_db(id)
  
  return  render_template("jobpagedetail.html", jobsbyid=job, Company="Parayil"  )
  

@app.route("/jobs/api/<id>")
def showjobapi_detail(id):
  job=load_job_from_db(id)
  return jsonify(job)  

if __name__=="__main__":
  print("i am inside you")
  app.run(host='0.0.0.0', debug=True)