from flask import Flask, jsonify, request, render_template
import os
from google import genai
from dotenv import load_dotenv
import requests
import json
import re

load_dotenv()

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
app = Flask(__name__, template_folder="templates")   

@app.route('/', methods=['GET', 'POST']) 
def generate_text():
    if request.method == 'POST':
        link = request.form.get('url')
        
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            quickly summarize the following transcript In less than 10 bullet points and make it like  easily readable notes based on this transcript also do not mention the transcript in your answer explain asthough you are teaching someone 0:00
- [Instructor] So let's just start with polar coordinates.
0:02
So let's say I have the coordinates.
0:03
So our radius is seven
0:05
and our angle in radians is three pi over five.
0:10
Pause the video and see if you can convert that
0:13
into rectangular coordinates.
0:14
Well, the key here is to recognize
0:17
that x is going to be equal to r cosine of theta
0:21
and y is going to be equal to r sine of theta.
0:25
So in this situation, our x coordinate,
0:28
I could write it like this.
0:29
It's going to be seven times cosine of three pi over five,
0:33
three pi over five,
0:36
and then our y coordinate
0:37
is going to be seven times sine of three pi over five.
0:43
Now this is correct,
0:45
but if we actually wanted to approximate
0:48
what numbers these are,
0:49
we could put them into our calculator.
0:52
So here we have our calculator.
0:55
Let's make sure we're in radian mode.
0:56
Yep, we are in radian mode,
0:58
and so if you were to take three times pi
1:02
divided by five, that's that, times cosine.
1:06
Not times cosine.
1:07
We're taking the cosine of it times seven.
1:12
Seven is equal to, I'll round to three decimal places,
1:15
so -2.163 approximately.
1:18
So this is, that right over there
1:21
is approximately -2.163,
1:24
and then if we were to do the same thing for the y value,
1:29
we would take, once again, three times pi divided by five
1:35
is equal to take the sine of that
1:38
and then multiply that times seven.
1:40
That's approximately 6.657.
1:43
So this is approximately 6.657.
1:48
Now let's look at an example where we go the other way
1:51
and let's do this one in degrees.
1:53
So let's say I was given the rectangular coordinates.
1:57
Let's say I'm given the rectangular coordinates -2,11.
2:01
Pause this video and try to write that as polar coordinates.
2:06
Well, in other videos we have seen
2:08
that r is going to be equal to
2:10
the square root of x squared plus y squared.
2:14
This comes straight outta the Pythagorean theorem,
2:17
and theta, theta is going to be equal to the inverse tan,
2:24
inverse tan of y over x.
2:27
Now we have to be careful here
2:29
because the inverse tan, let me give you an example here.
2:33
The inverse tangent, actually we'll do it,
2:35
we'll see it when we do this example.
2:36
If you just take the inverse tangent,
2:38
if we're thinking in degrees, it's gonna give you an angle
2:40
between negative 90 degrees and positive 90 degrees.
2:44
But we might have,
2:45
so something in the first or fourth quadrant,
2:47
but what about when the angle
2:48
is in the second or third quadrant?
2:51
So we have to think about that,
2:52
and we might be in a situation
2:54
where we want to add 180 degrees to it.
2:57
So maybe we could say, write +k times 180 degrees
3:02
where k is one or zero.
3:04
So maybe, yeah, that's a reasonable way to say it,
3:07
but another way to think about it is we might add,
3:09
so +180 degrees, I'll put in parentheses here,
3:14
where we're gonna have to think about where our angle is.
3:17
So let's start with r.
3:19
That's pretty straightforward,
3:20
r is going to be equal to the square root
3:22
of -2 squared is four, 11 squared is 121.
3:26
So it's equal to the square root of 125,
3:30
and now let's think about the inverse tangent.
3:33
So if I were to just take,
3:35
let's think about what quadrant we're in.
3:39
So this is our x-axis, that's our y-axis.
3:42
We're at -211,
3:43
so -211 I could think about being right over there.
3:47
So that's in the third quadrant,
3:50
so our r is gonna look like this, and this is our angle.
3:55
This is our angle right over here.
3:58
That's the theta we wanna solve for,
4:00
but if we take the inverse tangent of y over x,
4:04
it's actually going to give us...
4:06
It's actually going to give us,
4:08
it's actually going to give us this theta.
4:11
Maybe I'll call that theta prime.
4:13
So what we wanna do in this situation is whatever,
4:16
when I take the inverse 10 of y over x,
4:18
I want to add 180 degrees to it to get to our actual theta.
4:22
So in this situation, theta is going to be equal
4:25
to the inverse tangent of y over x,
4:28
so that's -11/2 or 11/-2, which is -11 halves,
4:33
and then plus 180 degrees
4:35
if we are doing this all in degrees.
4:38
So let's get our calculator out.
4:42
So that first part,
4:44
we could just straight up take the square root of 125,
4:48
so it's roughly 11.1.
4:52
I'll go to three decimal places again, 11.180.
4:56
I'll just do 11.18.
4:58
So this is approximately 11.18, and then the angle,
5:05
let's make sure that we are in degrees
5:07
'cause we wanna do this one in degrees.
5:08
We could have done it in radiance,
5:09
in which case we wouldn't be adding 180 degrees.
5:12
We'd be adding pi if we were doing it in radiance.
5:14
But let's now, whoops, I'm trying to clear this out.
5:18
Alright, I wanna take 11 divided by two.
5:22
Well, that could have done that in my head,
5:25
and then I wanna take the negative of that,
5:26
and then I wanna take the inverse tangent.
5:27
I don't see tangent.
5:28
I have to press second here,
5:29
and I have inverse tangent of that,
5:31
and notice it gave me the angle
5:33
of -79 point whatever whatever degrees.
5:36
I have to add 180 degrees to get to my actual angle.
5:39
So plus 180 is equal to 100, roughly a 100.3 degrees.
5:48
So theta is approximately 100.3 degrees.
5:53
So if I were to write it in polar coordinates,
5:55
that leaves the approximations.
5:56
It's 11.18,100.3 degrees, and I'm done.
            """
        )
        
        summary = response.text
        
       
        flashcard_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Based on the following summary about polar coordinates, create exactly 5 flashcards. 
            Return ONLY a valid JSON array with this exact structure:
            [
                {{"question": "What is the formula to convert from polar to rectangular coordinates?", "answer": "x = r*cos(θ) and y = r*sin(θ)"}},
                {{"question": "Another question here", "answer": "The corresponding answer here"}}
            ]
            
            Do not include any other text, explanations, or formatting. Just return the pure JSON array.
            
            Create a Summary with only relevant information and bullet points: {summary}
            """
        )
        
        print("Raw flashcard response:", flashcard_response.text)
        
        
        flashcards = []
        try:
            
            json_text = flashcard_response.text.strip()
            
            
            if json_text.startswith('```json'):
                json_text = json_text[7:] 
            if json_text.endswith('```'):
                json_text = json_text[:-3]
            
            json_text = json_text.strip()
            
            
            flashcards = json.loads(json_text)
            
            
            flashcards = flashcards[:5] 
            
            print("Parsed flashcards:", flashcards)
            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Raw text: {flashcard_response.text}")
            
            flashcards = [
                {"question": "What is the formula to convert from polar to rectangular coordinates?", 
                 "answer": "x = r*cos(θ) and y = r*sin(θ)"},
                {"question": "What is the formula to find r when converting from rectangular to polar?", 
                 "answer": "r = √(x² + y²)"},
                {"question": "What adjustment might be needed when finding θ using arctan?", 
                 "answer": "Add 180° (or π radians) if the point is in quadrant II or III"},
                {"question": "What calculator mode should be used for radian angles?", 
                 "answer": "Radian mode"},
                {"question": "What theorem is used to calculate r in polar coordinates?", 
                 "answer": "Pythagorean theorem"}
            ]
        
        return render_template('summaryflash.html', summary=summary, flashcards=flashcards)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)