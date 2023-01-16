

sdir = "../Chatbot/sylsound/"
import wave
def createsound(sounds , name):
        infiles = sounds
        outfile = sdir + name
        data= []                
        for infile in infiles:
            w = wave.open(infile, 'rb')
            print(infile)
            data.append( [w.getparams(), w.readframes(w.getnframes())] )
            w.close()
        output = wave.open(outfile, 'wb')
        output.setparams(data[0][0])
        output.setframerate(output.getframerate() * 2)
        for i in range(len(data)):
                    output.writeframes(data[i][1])
        output.close()


        
        
