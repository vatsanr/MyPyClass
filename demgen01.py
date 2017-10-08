from barnum import gen_data
import csv


with open('demographic.csv','w') as csvfile:
    csvwriter =csv.writer(csvfile, delimiter=' ')
    for i in range (0,100):
      name=gen_data.create_name()
      job_title=gen_data.create_job_title()
      phone=gen_data.create_phone()
      address=gen_data.create_city_state_zip()
      csvwriter.writerow([name,job_title,phone,address])

csvfile.close()
