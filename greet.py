from ladon.ladonizer import ladonize

# Create the service from the class and method

class Greeter():
    
    #use the ladonize decorator
    @ladonize(str,str,rtype=str)
    def greet(self,greeting,recipient):
        return f"{greeting},{recipient}"

