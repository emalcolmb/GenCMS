import cohere
import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide")

# Center the title using HTML and CSS
st.markdown("<h1 style='text-align: center;'>Generative Content Management System (GenCMS)</h1>", unsafe_allow_html=True)

st.write("The Generative Content Management System allows users to generate content for blogs and posts across social (X, LinkedIn, Facebook, Instagram) using the Cohere Command-R Large Language Model. The system ingests recent news and generates relevant, high-quality content that can be used by small business owners for content marketing purposes to drive organic traffic & conversions.")

# Initialize the Cohere client
co = cohere.Client(api_key="PVRDuwsakA7afOKKziEst9wdCrQE0N0Gnm17gIcY")

def create_html_template(article_text):
    """Create HTML content with embedded base64 image and user-provided text."""
    return f'''
    <h1>Compelling Title for the Blog Post</h1>
    <h2>Subtitle for Additional Context</h2>
    <h2>Introduction</h2>
    <p>{article_text}</p>
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#subheading1">Subheading 1</a></li>
        <li><a href="#subheading2">Subheading 2</a></li>
        <li><a href="#subheading3">Subheading 3</a></li>
    </ul>
    <h2>Main Content</h2>
    <h3 id="subheading1">Subheading 1</h3>
    <p>Details under subheading 1 with relevant keywords. This section delves into the first major point of the topic, providing in-depth information and insights.</p>
    <h3 id="subheading2">Subheading 2</h3>
    <p>Details under subheading 2 with relevant keywords. This part continues the exploration of the topic, focusing on another critical aspect.</p>
    <h3 id="subheading3">Subheading 3</h3>
    <p>Details under subheading 3 with relevant keywords. This section addresses the final major point, tying together the overall narrative of the blog post.</p>
    <h3>Interactive Elements and Social Proof</h3>
    <p>Include polls, quizzes, or testimonials here. Engaging the reader with interactive content can enhance their experience and increase retention.</p>
    <blockquote>Testimonial: "This blog changed my life!" - Happy Reader</blockquote>
    <h2>Related Articles</h2>
    <p>Explore more articles related to this topic to deepen your understanding and gain additional insights.</p>
    <ul>
        <li><a href="related-article-1.html">Related Article 1</a></li>
        <li><a href="related-article-2.html">Related Article 2</a></li>
        <li><a href="related-article-3.html">Related Article 3</a></li>
    </ul>
    <h2>Conclusion</h2>
    <p>This is the conclusion where you summarize the key points and reinforce the main message.</p>
    <h2>Call to Action</h2>
    <p>Don't forget to <a href="#subscribe">subscribe</a> for more updates!</p>
    <meta name="description" content="This is an SEO-optimized description of the blog post.">
    <meta name="keywords" content="keyword1, keyword2, keyword3">
    '''

def update_blog_post(persona, html_content):
    """Perform an API call to update the blog post with a comedian's style."""
    response = co.chat(
        model="command-r",
        message=f"Please update only the content (NOT the structure) of this Blog template in the voice, tone, and style of {persona} based on {persona}'s most likely reaction to this content: {html_content}. Make sure you update the headers (h1, h2) and paragraph (p) elements of the HTML to have a very similar style of {persona}. Also make sure the content in the paragraphs (p) do not exceed 1500 words in total. Your response must include the updated HTML elements (h1, h2, p etc), in the same structure and order just with updated content."
    )
    return response.text

def process_and_create_html(article_text, persona):
    """Update blog post with comedian's style and create HTML content."""
    html_template = create_html_template(article_text)
    updated_html_content = update_blog_post(persona, html_template)
    return updated_html_content

# Create two columns
col1, col2 = st.columns([2, 1])

# Dropdown selector for Content Type in the first column
content_type = col2.selectbox("Select Content Type:", ["Blog Post", "Lead Magnet", "X Post", "Facebook Post", "Instagram Post", "LinkedIn Post"])

# Dropdown selectbox for comedian selection
persona = col2.selectbox(
    "Select a persona:",
    ["Matt Taibbi", "Andrew Ross Sorkin", "Rebecca Quick", "Kara Swisher", "John Gruber", "Casey Newton", "Jeff Ross", "Jerry Seinfeld", "Dave Chappelle", "Joan Rivers", "Louis C.K.", "Sam Altman", "Geoffrey Hinton"]
)

# Text area for news article text
article_text = col1.text_area("Enter News Article Text", height=170)

# Display the dataframe at the bottom of the page (if applicable)
# if 'df' in locals() and not df.empty:
#     st.dataframe(df)

# Generate content button
if col1.button("Generate Content"):
    html_content = process_and_create_html(article_text, persona)
    
    # Show the rendered HTML content
    col1.markdown(html_content, unsafe_allow_html=True)

    # Show the HTML code itself
    #st.code(html_content, language='html')
    
        # Show the HTML code itself in col2
    #col2.subheader("Generated HTML Code:")
    col2.code(html_content, language='html')
