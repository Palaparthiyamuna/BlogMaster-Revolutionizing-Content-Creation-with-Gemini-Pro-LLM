import streamlit as st
 
import google.generativeai as genai
 
import random
 

 
# Configure your Google Generative AI API key
 
API_KEY = "AIzaSyD-EGqrpeudmbJVrGDwT9Mtd5NZpOWbCU8"  # Replace with your actual API key
 
genai.configure(api_key=API_KEY)
 

 
# Configure model generation settings
 
generation_config = {
 
    "temperature": 0.75,
 
    "top_p": 0.95,
 
    "top_k": 64,
 
    "max_output_tokens": 8192,
 
    "response_mime_type": "text/plain",
 
}
 

 
# Create the generative model instance
 
model = genai.GenerativeModel(
 
    model_name="gemini-1.5-pro",
 
    generation_config=generation_config,
 
)
 

 
# Function to generate a joke
 
def get_joke():
 
    jokes = [
 
        "Why do programmers prefer dark mode? Because light attracts bugs!",
 
        "Why did the developer go broke? Because he used up all his cache!",
 
        "Why do Java developers wear glasses? Because they don't see sharp.",
 
        "Why don't programmers like nature? It has too many bugs.",
 
    ]
 
    return random.choice(jokes)
 

 
# Function to generate a blog
 
def generate_blog(user_input, word_count):
 
    st.write("### ⏳ Generating Your Blog...")
 
    st.write(f"🤖 Here's a joke while you wait:\n\n*{get_joke()}*")
 

 
    chat_session = model.start_chat(
 
        history=[
 
            {
 
                "role": "user",
 
                "parts": [
 
                    f"Write a blog about: {user_input}, with {word_count} words.",
 
                ],
 
            },
 
        ]
 
    )
 

 
    try:
 
        # Generate a response
 
        response = chat_session.send_message(user_input)
 
        st.success("🎉 Your blog is ready!")
 
        return response.text if response else "No response received."
 

 
    except Exception as e:
 
        st.error(f"❌ Error generating blog: {e}")
 
        return None
 

 
# Streamlit UI
 
def main():
 

    st.title("📖 BlogMaster: AI-Powered Blog Generation")
 

    st.title("📖 BlogMaster: Revolutionizing Content Creation with Gemini Pro LLM")
 

 
    # Display the second image at the top
 
    st.image("edited_blog_master.jpg", use_container_width=True)  # ✅ Fixed error here
 

 
    st.write("### 🤖 Hello! I'm BlogMaster. Let's create an amazing blog!")
 

 
    # User inputs
 
    user_input = st.text_input("Enter your blog topic:")
 
    word_count = st.number_input("Number of words", min_value=100, max_value=5000, value=1000, step=50)
 

 
    if st.button("Generate Blog"):
 
        if user_input and word_count:
 
            blog_content = generate_blog(user_input, word_count)
 
            if blog_content:
 
                st.write("### 📝 Your AI-Generated Blog:")
 
                st.write(blog_content)
 
        else:
 
            st.error("⚠ Please enter both the topic and the number of words.")
 

 
if _name_ == "_main_":
 
    main()
