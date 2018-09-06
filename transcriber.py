import speech_recognition as sr
from os import path
from pydub import AudioSegment


def transcribe_wav(AUDIO_FILE):
	# use the audio file as the audio source                                        
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)  # read the entire audio file                  

		print("Transcription: " + r.recognize_google(audio))


# convert mp3 file to wav                                    
sound = AudioSegment.from_mp3("gregglassman.mp3")
# get 30 seconds each
soundLen = len(sound)
segment_size = 10 * 10000
segments = int(soundLen / segment_size) + 1
print(soundLen)
print(segments)
for segment in range(0, segments):
	if (segment+1)*segment_size > soundLen:
		sound_segment = sound[segment*segment_size:]
	else:
		sound_segment = sound[segment*segment_size:(segment+1)*segment_size]
	
	audio_file = "transcript{}.wav".format(segment)
	sound.export(audio_file, format="wav")
	# transcribe audio file                                                         
	transcribe_wav(audio_file)

	