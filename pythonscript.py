from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import InferenceClient
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound


#Text generator
def text_generator(prompt):
    client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct",
    token="hf_(TOKEN_KEY)",)
    result=''
    
    for message in client.chat_completion( messages=[{"role": "user", "content": prompt}],max_tokens=500,stream=True,):
        result=result+ " "+ message.choices[0].delta.content
    return result

#extract the first string
def extract_first_string(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        first_string = content.split()[0]
        return first_string



#clear the text file
def file_clear(file_path):
    with open(file_path, "w") as file:
        pass
    
#text to speech   
def text_speech(text):
    output_file='result_audio.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    playsound(output_file)


if __name__ == "__main__":
    
    prompt=extract_first_string('prompt.txt')
    file_clear('prompt.txt')
    prompt = "how to make "+prompt +" step wise."
    longer_text=text_generator(prompt)
    modified_string = longer_text.replace('*', '')
    print("\nLonger Generated Text:\n", modified_string)
    with open("result.txt", "w") as file:
        file.write(modified_string)
    text_speech(modified_string)
    
