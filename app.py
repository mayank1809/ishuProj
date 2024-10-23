import gradio as gr
from app.search_interface import search_courses

# Function for the search tool
def search_tool(query):
    results = search_courses(query)
    # Format the results to display
    formatted_results = "\n\n".join(
        [f"Title: {course['title']}\nDescription: {course['description']}" for course in results]
    )
    return formatted_results

# Create a Gradio interface
interface = gr.Interface(fn=search_tool, 
                         inputs="text", 
                         outputs="text",
                         title="Analytics Vidhya Free Courses Search",
                         description="Enter a query to search for free courses.")

if __name__ == "__main__":
    # Launch the Gradio app
    interface.launch()
