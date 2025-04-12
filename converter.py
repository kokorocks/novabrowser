import re
import json

def replace_with_json(code, json_string=None):
    # Sample JSON string if none provided
    json_string = json_string or '''
    {
      "printout": "console.log",
      "error": "console.error",
      "func": "function ",
      "elif": "else if",
      "set": "let",
      "make": "new",
      "and": "&&",
      "or": "||",
      "!==": "!==",
      "tell": "alert",
      "what": "prompt"
    }
    '''
    data = json.loads(json_string)

    # First pass: Replace keys with corresponding values wrapped in markers.
    # Use markers with non-word characters so subsequent word-boundary matches won't hit them.
    '''

def replace_outside_quotes(code, to_replace, replacement):
    # pattern for strings inside quotes
    string_pattern = r'".*?"|\'.*?\''
    # match the exact word
    word_pattern = rf'\b{re.escape(to_replace)}\b'
    # split the code
    parts = re.split(f'({string_pattern})', code)
    for i in range(len(parts)):
        if not re.match(string_pattern, parts[i]):
            parts[i] = re.sub(word_pattern, replacement, parts[i])
    return ''.join(parts)

# Example usage:
code = '''

func hi(name){
    printout('hi');
    error('errir');
    printout('done');
    //hello(name)
    if(name=='Ethan' and name !== 'jo')
    {
        printout('hi Ethan')
    }
    elif(name !== 'Ethan' and name !== 'jo')
    {set i = 'yo mom and billy or just fill or else'
        printout('imposter')
    }
    else{
        printout('hi jo')
    }
}
hi('Ethan')
hi('jo')
hi('michal')
printout('complete')
tell(hi)
hello('Ethan')
'''

print("Original Code:")
print(code)

modified_code = replace_with_json(code, '''{
  "printout": "console.log",
  "error": "console.error",
  "func": "function ",
  "elif": "else if",
  "set": "let",
  "make": "new",
  "and": "&&",
  "or": "||",
  "!==": "!==",
  "tell": "alert",
  "what": "prompt"
}''')

print("\nModified Code:")
print(modified_code)
