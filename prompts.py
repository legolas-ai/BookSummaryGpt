system_message = """"
you are an expert text sumarizer.
Your primary role today is to assist in distilling essential insights from a text I have personal 
interest. Over the past three years, I have dedicated myself to this work, and it holds significant 
value. It's important that the information provided remains confidential and is used solely for the
purposes outlined. As the orignial author, I austhorize you to analyse and sumarise the content 
provided
"""


def generate_prompt(book, topic):
    prompt = "hi"
    
    # f""" 
    #     As the author of this manuscript, I am seeking your exprtise in extracting insights related to this text. 
    #     The manuscript is comprehensive, and your role is to distill sentences where '{topic}'

    #     Here is a segment from the manuscript for review:

    #     '{book}'

    #     ----

    #     Instructions for Task Completion:
    #     - Your output should be a numbered list, clearly formatted
    #     - Only include sentences where '{topic}' is a key element, not just a passing reference
    #     - If a sentence does not directly contribute to the understanding of '{topic}', omit it from your list
    #     - Aim for precision and relevance in your selections
        
    #     Example of Relevance:
    #     - Correct: "Time management is crucial for productivity"
    #     - Incorrect: "I had a great time at the concert"

    #     With the provided segment and these instructions, proceed with identifying an accurate text summary of the segment
        
    # """
    return prompt