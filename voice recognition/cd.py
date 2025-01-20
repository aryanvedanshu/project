import wave

obj = wave.open("prc.wav", "rb")

print("no. of Channels",obj.getnchannels())
print("Space Width", obj.getsampwidth())
print("Frame Rate", obj.getframerate())
print("No. of Frames ", obj.getnframes())
print("Parameters", obj.getparams())

t_audio = obj.getnframes()/obj.getframerate()
print("t_audio", t_audio)

frames = obj.readframes(-1)
print(type(frames), frames[56], type(frames[1]))
print("lenght of frames", len(frames))

obj.close()

obj_new = wave.open("prc_new.wav", 'wb')

#If channel is increased then the duration of audio Sticked also if sample width is made twice then the effect is neglected

#The higher the frame rate, the faster the music goes

obj_new.setnchannels(2) 
obj_new.setsampwidth(2)
obj_new.setframerate(50000)


obj_new.writeframes(frames)
t_new_audio = obj_new.getnframes()/obj_new.getframerate()
print("t_new_audio", t_new_audio)

obj_new.close()