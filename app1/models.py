from django.db import models

class Agent(models.Model):
	email = models.CharField(max_length=50)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	father_name= models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	address= models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	profile_photo= models.CharField(max_length=30)
	cover_photo= models.CharField(max_length=30,null=True)
	phone= models.CharField(max_length=30)
	whats_phone= models.CharField(max_length=30)
	points=models.PositiveBigIntegerField()

	gender = models.CharField(max_length=10)
	marital_status = models.CharField(max_length=20)
	children_number = models.CharField(max_length=20)
	current_work = models.CharField(max_length=50)
	previous_work = models.CharField(max_length=50)
	current_address = models.CharField(max_length=50)
	previous_address = models.CharField(max_length=50)
	weight = models.CharField(max_length=20)
	height = models.CharField(max_length=20)
	is_smoker = models.IntegerField()
	cigaretes_number = models.CharField(max_length=20,null=True)
	alcoholic = models.CharField(max_length=20)
	Hookah = models.CharField(max_length=20)
	is_sensitive_from_medicine=models.IntegerField()
	sensitivy_medicines=models.CharField(max_length=50,null=True)
	is_sensitive_from_bugs=models.IntegerField()
	is_sensitive_from_illnesses=models.IntegerField()
	sensitivity_illnesses_names=models.CharField(max_length=50,null=True)
	#chronic diseases
	sugar=models.IntegerField()
	pressure=models.IntegerField()
	heart=models.IntegerField()
	#previous diseases
	corona=models.IntegerField()
	smallpox=models.IntegerField()
	other_previous_illnesses=models.CharField(max_length=50,null=True)
	#previous Surgery::::::
	tonsils=models.IntegerField()
	appendix=models.IntegerField()
	bitterness=models.IntegerField()
	other_previous_surgeries=models.CharField(max_length=50,null=True)
	#blood::::::
	blood_type=models.CharField(max_length=20)
	blood_donation_number=models.IntegerField()
	blood_getting_number=models.IntegerField()
	family_diseases=models.CharField(max_length=20)
	previous_medicenes=models.CharField(max_length=20)
	current_medicines=models.CharField(max_length=20)
	analysis_names=models.CharField(max_length=20,null=True)
	#analysis images UserMedicalAnalysisImages
	#X-ray images::::::
	xrays_images_names=models.CharField(max_length=20,null=True)
	#xrays_images UserXRayImages	
	class Meta:
		abstract = True

class Doctor(Agent):
	cv=models.CharField(max_length=20,null=True)
	university=models.CharField(max_length=20,null=True)
	college= models.ForeignKey("College", on_delete=models.CASCADE)
	specialty= models.ForeignKey("Specialty", on_delete=models.CASCADE)
	graduation_year=models.CharField(max_length=20,null=True)
	
class DoctorDays(models.Model):
	doctor= models.ForeignKey("Doctor", on_delete=models.CASCADE)
	day=models.CharField(max_length=20,null=True)
	period_start_am=models.CharField(max_length=20,null=True)
	period_end_am=models.CharField(max_length=20,null=True)
	period_start_pm=models.CharField(max_length=20,null=True)
	period_end_pm=models.CharField(max_length=20,null=True)

class DoctorLanguages(models.Model):
	doctor= models.ForeignKey("Doctor", on_delete=models.CASCADE)
	language=models.CharField(max_length=20,null=True)
class DoctorJobs(models.Model):
	doctor= models.ForeignKey("Doctor", on_delete=models.CASCADE)
	job=models.CharField(max_length=20,null=True)
class DoctorCertificate(models.Model):
	doctor= models.ForeignKey("Doctor", on_delete=models.CASCADE)
	name=models.CharField(max_length=20,null=True)
	image=models.ImageField(upload_to='/DoctorCertificate')
	
class College(models.Model):
	name=models.CharField(max_length=20)
class Specialty(models.Model):
	name=models.CharField(max_length=20)

class Pharmacist(Agent):
	#is_active (points and manuel check)
	cv=models.CharField(max_length=20,null=True)
	university=models.CharField(max_length=20,null=True)
	college= models.ForeignKey("College", on_delete=models.CASCADE)
	specialty= models.ForeignKey("Specialty", on_delete=models.CASCADE)
	graduation_year=models.CharField(max_length=20,null=True)
	
class PharmacistDays(models.Model):
	pharmacist= models.ForeignKey("Pharmacist", on_delete=models.CASCADE)
	day=models.CharField(max_length=20,null=True)	
class PharmacistLanguages(models.Model):
	pharmacist= models.ForeignKey("Pharmacist", on_delete=models.CASCADE)
	language=models.CharField(max_length=20,null=True)		
class PharmacistJobs(models.Model):
	pharmacist= models.ForeignKey("Pharmacist", on_delete=models.CASCADE)
	job=models.CharField(max_length=20,null=True)
class PharmacistCertificate(models.Model):
	pharmacist= models.ForeignKey("Pharmacist", on_delete=models.CASCADE)
	name=models.CharField(max_length=20,null=True)
	image=models.ImageField(upload_to='/DoctorCertificate')
	
class User(Agent):
	pass


class MedicalAnalysisImages(models.Model):
	agent=models.ForeignKey("Agent", on_delete=models.CASCADE) 
	image=models.ImageField(upload_to='/UserMedicalAnalysisImages')
	
class XRayImages(models.Model):
	agent=models.ForeignKey("Agent", on_delete=models.CASCADE) 
	image=models.ImageField(upload_to='/UserXRayImages')

	
class DoctorPosts(models.Model):
	doctor= models.ForeignKey("Doctor", on_delete=models.CASCADE)
	text = models.CharField(max_length=10,null=True)
	image = models.CharField(max_length=20,null=True)
	video = models.CharField(max_length=20,null=True)
	#file

class PharmacistPosts(models.Model):
	pharmacist= models.ForeignKey("Pharmacist", on_delete=models.CASCADE)
	text = models.CharField(max_length=10,null=True)
	image = models.CharField(max_length=20,null=True)
	video = models.CharField(max_length=20,null=True)
	#file
	
class PostsReactions(models.Model):	
	agent= models.ForeignKey("Agent", on_delete=models.CASCADE)
	#post
	type = models.IntegerField()# 0 for like 1 for love

class DoctorAdvertisement(models.Model):
	doctor= models.ForeignKey("Doctor", on_delete=models.CASCADE)
	text= models.CharField(max_length=20,null=True)
	image= models.CharField(max_length=20,null=True)
	
class PharmacistAdvertisement(models.Model):
	pharmacist= models.ForeignKey("Pharmacist", on_delete=models.CASCADE)
	text= models.CharField(max_length=20,null=True)
	image= models.CharField(max_length=20,null=True)
	
class Active(models.Model):
	agent= models.ForeignKey("Agent", on_delete=models.CASCADE)
	
class Follow(models.Model):
	agent1= models.ForeignKey("Agent", on_delete=models.CASCADE)
	agent2= models.ForeignKey("Agent", on_delete=models.CASCADE)
	
class Help(models.Model):
	agent= models.ForeignKey("Agent", on_delete=models.CASCADE)
	text= models.CharField(max_length=100,null=True)
	#video one
	
class HelpImages(models.Model):
	help= models.ForeignKey("Help", on_delete=models.CASCADE)
	image=models.ImageField(upload_to='/HelpImages')

class Consult(models.Model):
	agent= models.ForeignKey("Agent", on_delete=models.CASCADE)
	text= models.CharField(max_length=100,null=True)
	#اختصاص
	#private or public medical profile of patient
	#images 

class ConsultResponse(models.Model):
	agent= models.ForeignKey("Agent", on_delete=models.CASCADE)
	response= models.CharField(max_length=100,null=True)
	#date autonow

	
#DoctorBook
#PharmacistBook

#locations
#offers
#اهداءات ِ Agent Agent

#Recommendations: agent - agent

#Story
#Reactions love like
