import json
import math
def load_journal(filename):
	f=open(filename,"r")
	list_dict=json.load(f)
	f.close()
	return list_dict

def compute_phi(filename,event):
	list_dict=load_journal(filename)
	reference={"n11":"var1","n00":"var2","n10":"var3","n01":"var4","n1+":"var5","n0+":"var6",
"n+1":"var7","n+0":"var8"}
	var1=var2=var3=var4=var5=var6=var7=var8=0
	for i in list_dict:

		if  event in i['events']:
			var5+=1
			if  i['squirrel']==True:
				var7+=1
				var1+=1
			else:
				var8+=1
				var3+=1
		else:
			var6+=1
			if  i['squirrel']==True:
				var7+=1
				var4+=1
			else:
				var8+=1
				var2+=1
	num=(var1*var2)-(var3*var4)		
	den=math.sqrt(var5*var6*var7*var8)
	corr_val=num/den
	return corr_val
	
def compute_correlations(filename):
	list_dict=load_journal(filename)
	result_dict={}
	for i in list_dict:
		for j in i['events']:
			corr_val=compute_phi(filename,j)
			if j not in result_dict:
				result_dict[j]=corr_val
	return result_dict
		
def diagnose(filename):
	result_dict=compute_correlations(filename)
	max_val=min_val=0
	for key,value in result_dict.items():
		if value>=0:
			if value>max_val:
				max_val=value
				max_val_key=key
		else:
			if value<min_val:
				min_val=value
				min_val_key=key
	return max_val_key,min_val_key
		
			
	

	

