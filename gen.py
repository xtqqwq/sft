import json

def read_jsonl(file_path):
	with open(file_path, 'r') as file:
		for line in file:
			yield json.loads(line)

# Example usage
file_path = 'data.jsonl'
output_file_path = 'output.jsonl'
with open(output_file_path, 'w') as output_file:
	for record in read_jsonl(file_path):
		if record.get('question', {}).get('ground_truth_answer') == record.get('question', {}).get('pre_generated_answer'):
			new_record = {
				"input": record.get('question', {}).get('problem'),
				"output": '\n\n'.join(record.get('question', {}).get('pre_generated_steps', []))
			}
			output_file.write(json.dumps(new_record) + '\n')