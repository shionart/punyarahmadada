from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
import requests
import json


from indonesia.rekomendasi_kalor import optimasi_beban_unit



# Create your views here.

def indeks (request):
	konteks={}
	if request.method == 'POST':
		Preq=int(request.POST['targetkalor']	)
		coef_pembebanan =[(15.59,443872.57,8854230.19),(432.52,228835.28,26186478.79),(928.68,-130876.67,81788363.85)]
		min_dn = 200
		max_dn = 315
		hasil1,hasil2,hasil3 = optimasi_beban_unit(coef_pembebanan,Preq,min_dn,max_dn)
		jsonnya = {
			'nilaikalor' : hasil1,
			'totalmoisture' :hasil2,
			'totalsulfur' : hasil3}
		# konteks=jsonnya
		# return JsonResponse(konteks, safe=False)
		return render(request, 'indeks.html', jsonnya)
	title = "Indonesia Power"
	nama = "Aburizal Khatami"
	return render(request, 'indeks.html', konteks)

def detail (request):
	with open('Z:\projectWeb\django\project\data_blending.json') as f:
		samlekom = json.load(f)
	
	# result = the_dict   
	# for key in keys:     
	# 	if hasattr(result, 'get'):       
	# 		result = result.get(key, '')     
	# 	else:       
	# 		break   
	# 	return result
	konteks = {
		'pemasok1' : samlekom[0],
		'pemasok2' : samlekom[1]
	}
	
	
	
	# print("nomor : "+str(pemasok1['Pemasok']))
	# return samlekom
	return render(request, 'detail.html', konteks)

def tabeel (request):

	konteks = {}
	return render(request, 'tabeel.html', konteks)

def coba(request):
	with open('Z:\projectWeb\django\project\data_blending.json') as f:
		samlekom = json.load(f)

	# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
	return JsonResponse(samlekom, safe=False)
	# return JsonResponse(jsonnya, safe=False)
	
	# return redirect(to='/indeks', )
	# return render(request, 'indeks.html', hasil)