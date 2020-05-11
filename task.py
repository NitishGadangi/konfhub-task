import requests,csv

def difference_dict(Dict_A, Dict_B):
    diffs = 0
    for key in Dict_A.keys():
        if Dict_A[key] != Dict_B[key]:
        	diffs+=1
    return diffs

def get_json_response():
	API_URL="https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"
	req=requests.get(API_URL)
	json_response=req.json()
	return json_response

def get_all_conferences(json_response):
	all_conference=[]
	paid_conf=json_response['paid']
	print(f"\n....{len(paid_conf)} paid conferences")
	# all_conference.append(paid_conf)
	free_conf=json_response['free']
	print(f"....{len(free_conf)} free conferences")
	# all_conference.append(free_conf)
	return paid_conf+free_conf

def print_content(all_conferences):
	for conference in all_conferences:
		req_values=[conference['confName'],conference['confStartDate'],conference['city'],conference['state'],conference['country'],conference['entryType'],conference['confRegUrl']]
		filtered_values=[x for x in req_values if x!=""]
		output=", ".join(filtered_values)
		print(output)

def remove_exact_and_semantic_duplicates(all_conferences):
	duplicates=[]
	for i in range(0,len(all_conferences)):
		for j in range(0,i):
			diff=difference_dict(all_conferences[i],all_conferences[j])
			if diff<=3:
				duplicates.append(all_conferences[i])
	return duplicates

def generate_csv(all_conferences):
	with open('output.csv', 'w') as f:
		w = csv.writer(f)
		w.writerow(all_conferences[0].keys())
		for conf in all_conferences:
			w.writerow(conf.values())
	print("\n***output.csv exported to current working direcrory***")


if __name__ == "__main__":
	print("Hello World")

	print("\n....Fetching Json Response from the API...")
	json_response=get_json_response()
	all_conferences=get_all_conferences(json_response)

	print("\n....searching exact and semantic duplicates...")
	duplicates=remove_exact_and_semantic_duplicates(all_conferences)
	print(f"\n....{len(duplicates)} duplicates found")
	print(f"....{len(all_conferences)} total conferences")
	print("\n....Filtering Done......\n\n")

	print("---Select an Option--")
	print("-> 1. Print the contents in a human readable format")
	print("-> 2. Print Duplicates")
	print("-> 3. Export the contents to csv")
	option=int(input("option(1/2/3): "))
	if option is 1:
		print_content(all_conferences)
	elif option is 2:
		print_content(duplicates)
	elif option is 3:
		generate_csv(all_conferences)
	else:
		print("\nYou have entered a wrong input\n\n restart the program again")

