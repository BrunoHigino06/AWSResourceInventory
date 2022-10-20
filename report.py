with open('report_json.json', 'r+') as file:
    content = file.read()
    file.seek(0)
    content.replace('I', 'aa')
    file.write(content)