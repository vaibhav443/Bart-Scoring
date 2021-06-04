from Utils_grader import *

params = {
    "Normal_kwds" : ["sofa", "couch", "furniture", "sleeper sofa", "inches", "Modern sofa", "living face", "piece of furniture", "size", "small space"],
    "Heading_kwds" : [""],
    "text" : "Buying a sofa is one of the most important purchases you can make for your home: It should look great, feel comfortable, and hold up to extended use. There are so many options to choose from and couches can cost anywhere from hundreds to thousands of dollars, so you want to make sure you’re spending your money on a high quality sofa that’s worth the splurge.",
    "frequencies" : [42,54,65]# frequencies of each keyword in the serp results.

}
def Content_grader(params):
    dict_ = content_grader(params.get("Normal_kwds"),params.get("text"))
    gradings,keywords = grader(dict_,0.8)
    dict_res = {}
    dict_res["kwds"] = keywords
    dict_res["grade"] = gradings
    return dict_res

dict_res = Content_grader(params)
print(dict_res)