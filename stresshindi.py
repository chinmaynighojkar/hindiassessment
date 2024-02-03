import streamlit as st

def categorize_stress_level(total_score):
    if total_score <= 13:
        return "आपका कम तनाव है।"
    elif 14 <= total_score <= 26:
        return "आपका मामूल्य तनाव है।"
    else:
        return "आपका अधिक मान्यता वाला तनाव है।"
    
def survey_question_1():
    st.markdown("### पिछले महीने, आपने अचानक हुए किसी घटना के कारण कितनी बार दुखी हुए?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 1 के लिए एक विकल्प चुनें:", options, index=None, key="question1")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "काफी अक्सर": 3, "बहुत अक्सर": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_2():
    st.markdown("### पिछले महीने, कितनी बार आपको ऐसा लगा कि आप अपने जीवन की महत्वपूर्ण बातें नहीं कंट्रोल कर सकते थे?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 2 के लिए एक विकल्प चुनें:", options, index=None, key="question2")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "काफी अक्सर": 3, "बहुत अक्सर": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_3():
    st.markdown("### पिछले महीने, कितनी बार आपको ऐसा लगा कि आप घबराएं और तनाव में थे?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 3 के लिए एक विकल्प चुनें:", options, index=None, key="question3")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "काफी अक्सर": 3, "बहुत अक्सर": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_4():
    st.markdown("### पिछले महीने, कितनी बार आपको ऐसा लगा कि आप सभी चीजों का सामना नहीं कर सकते थे?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 4 के लिए एक विकल्प चुनें:", options, index=None, key="question4")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "काफी अक्सर": 3, "बहुत अक्सर": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_5():
    st.markdown("### पिछले महीने, कितनी बार आपको ऐसा लगा कि आप वह चीजें जो हुई थीं उन पर आपका कोई नियंत्रण नहीं था?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 5 के लिए एक विकल्प चुनें:", options, index=None, key="question5")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "काफी अक्सर": 3, "बहुत अक्सर": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_6():
    st.markdown("### पिछले महीने, कितनी बार आपको ऐसा लगा कि कठिनाईयाँ इतनी ज्यादा बढ़ गई थीं कि आप उन्हें पार नहीं कर सकते थे?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 6 के लिए एक विकल्प चुनें:", options, index=None, key="question6")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "काफी अक्सर": 3, "बहुत अक्सर": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_7():
    st.markdown("### पिछले महीने, कितनी बार आपको ऐसा लगा कि आप अपनी व्यक्तिगत समस्याओं को संभालने की क्षमता में आत्मविश्वास था?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 7 के लिए एक विकल्प चुनें:", options, index=None, key="question7")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 4, "लगभग कभी नहीं": 3, "कभी-कभी": 2, "काफी अक्सर": 1, "बहुत अक्सर": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_8():
    st.markdown("### पिछले महीने, कितनी बार आपको ऐसा लगा कि चीजें आपके रास्ते में जा रही थीं?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 8 के लिए एक विकल्प चुनें:", options, index=None, key="question8")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 4, "लगभग कभी नहीं": 3, "कभी-कभी": 2, "काफी अक्सर": 1, "बहुत अक्सर": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_9():
    st.markdown("### पिछले महीने, कितनी बार आपने अपने जीवन में कुचलने की क्षमता रखी थी?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 9 के लिए एक विकल्प चुनें:", options, index=None, key="question9")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 4, "लगभग कभी नहीं": 3, "कभी-कभी": 2, "काफी अक्सर": 1, "बहुत अक्सर": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_10():
    st.markdown("### पिछले महीने, कितनी बार आपको ऐसा लगा कि आप चीजों पर कुछ कर रहे थे?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 10 के लिए एक विकल्प चुनें:", options, index=None, key="question10")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 4, "लगभग कभी नहीं": 3, "कभी-कभी": 2, "काफी अक्सर": 1, "बहुत अक्सर": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score
    
def main():
    st.title("Survey App")

    # First question
    score1 = survey_question_1()

    # Second question
    score2 = survey_question_2()

    # Third question
    score3 = survey_question_3()

    # Fourth question
    score4 = survey_question_4()

    # Fifth question
    score5 = survey_question_5()

    # Sixth question
    score6 = survey_question_6()

    # Seventh question
    score7 = survey_question_7()

    # Eighth question
    score8 = survey_question_8()

    # Ninth question
    score9 = survey_question_9()

    # Tenth question
    score10 = survey_question_10()

    # Handle the case where no option is selected for any question
    if any(score is None for score in [score1, score2, score3, score4, score5, score6, score7, score8, score9, score10]):
        st.warning("Please select an option for all questions.")
        return

    # Calculate total score
    total_score = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
    
    # Display total score
    st.write(f"Total Score: {total_score}")

    # Categorize stress level and display result
    stress_level = categorize_stress_level(total_score)
    st.write(f"तनाव स्तर: {stress_level}")
  
if __name__ == "__main__":
    main()
