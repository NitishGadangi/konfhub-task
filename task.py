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

def print_content(all_conferences):
	for conference in all_conferences:
		req_values=[conference['confName'],conference['confStartDate'],conference['city'],conference['state'],conference['country'],conference['entryType'],conference['confRegUrl']]
		filtered_values=[x for x in req_values if x!=""]
		output=", ".join(filtered_values)
		print(output)

def remove_exact_and_semantic_duplicates(all_conferences):
	filtered=[]
	duplicates=[]
	for i in range(0,len(all_conferences)):
		for j in range(0,i):
			diff=difference_dict(all_conferences[i],all_conferences[j])
			print(diff)
			if diff<=3:
				duplicates.append(all_conferences[i])
			else:
				filtered.append(all_conferences[i])
	return filtered,duplicates

def generate_csv(all_conferences):
	with open('output.csv', 'w') as f:
		w = csv.writer(f)
		w.writerow(all_conferences[0].keys())
		for conf in all_conferences:
			w.writerow(conf.values())
	print("\n\n***output.csv exported to current direcrory***")


if __name__ == "__main__":
	print("Hello World")
