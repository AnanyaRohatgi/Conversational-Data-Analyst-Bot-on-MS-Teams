# from botbuilder.core import ActivityHandler, TurnContext
# from botbuilder.schema import ChannelAccount, Activity, Attachment
# from pandasai import SmartDataframe, SmartDatalake
# from pandasai.llm.azure_openai import AzureOpenAI
# import pandas as pd
# import io
# import base64
# import matplotlib.pyplot as plt

# # Initialize Azure OpenAI LLM
# llm = AzureOpenAI(
#     api_token="9RaBd2y8Q5SWaCXK4yZeaR0cUwsQVYQduQgTDoy5SXFkHcf35QXEJQQJ99BBACYeBjFXJ3w3AAAAACOGBVjL",
#     azure_endpoint="https://aiservices-eus-qlik-hzl-prod-spk-si.cognitiveservices.azure.com",
#     api_version="2024-08-01-preview",
#     deployment_name="eus-gpt-4",
# )

# # File paths
# excel_file = r"C:\Users\ANANYA ROHATGI\OneDrive\Desktop\teamsbot\merged_file_correct.xlsx"
# csv_file = r"C:\Users\ANANYA ROHATGI\OneDrive\Desktop\teamsbot\Key Metrics.csv"

# # Read Excel file (first sheet)
# dfs = pd.read_excel(excel_file, sheet_name=None)
# df_main = list(dfs.values())[0]  # Take the first sheet as the primary DataFrame

# # Read CSV file
# df_metrics = pd.read_csv(csv_file)

# # Convert DataFrames to SmartDataframes
# sdf1 = SmartDataframe(df_main, config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True})
# sdf2 = SmartDataframe(df_metrics, config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True})

# # Combine both DataFrames into SmartDatalake
# data_lake = SmartDatalake([sdf1, sdf2], config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True})

# class MyBot(ActivityHandler):
#     async def on_message_activity(self, turn_context: TurnContext):
#         user_query = turn_context.activity.text
#         response = data_lake.chat(user_query)

#         if isinstance(response, str):
#             await turn_context.send_activity(response)

#         elif isinstance(response, pd.DataFrame):
#             df_string = response.to_string(index=False)
#             await turn_context.send_activity(f"Here are the results:\n```\n{df_string}\n```")

#         elif isinstance(response, dict) or isinstance(response, list):
#             await turn_context.send_activity(str(response))

#         elif isinstance(response, plt.Figure):  # If response is a matplotlib Figure
#             image_url = self.convert_figure_to_attachment(response)
#             await turn_context.send_activity(f"Here is your chart: {image_url}")

#         else:
#             await turn_context.send_activity("Unexpected response format.")

#     def convert_figure_to_attachment(self, fig):
#         """Convert a Matplotlib figure to a Base64 image and return as an attachment URL."""
#         img_stream = io.BytesIO()
#         fig.savefig(img_stream, format="png")  # Save figure as PNG in memory
#         img_stream.seek(0)
#         base64_str = base64.b64encode(img_stream.getvalue()).decode()

#         # Create attachment
#         return f"data:image/png;base64,{base64_str}"

#     async def on_members_added_activity(self, members_added, turn_context: TurnContext):
#         for member_added in members_added:
#             if member_added.id != turn_context.activity.recipient.id:
#                 await turn_context.send_activity("Hello and welcome!")
# from botbuilder.core import ActivityHandler, TurnContext
# from botbuilder.schema import ChannelAccount, Activity, Attachment
# from pandasai import SmartDataframe, SmartDatalake
# from pandasai.llm.azure_openai import AzureOpenAI
# import pandas as pd
# import io
# import base64
# import matplotlib.pyplot as plt
# import os
# import numbers

# # Initialize Azure OpenAI LLM
# llm = AzureOpenAI(
#     api_token="9RaBd2y8Q5SWaCXK4yZeaR0cUwsQVYQduQgTDoy5SXFkHcf35QXEJQQJ99BBACYeBjFXJ3w3AAAAACOGBVjL",  # Use environment variables for security
#     azure_endpoint="https://aiservices-eus-qlik-hzl-prod-spk-si.cognitiveservices.azure.com",
#     api_version="2024-08-01-preview",
#     deployment_name="eus-gpt-4",
# )

# # File paths
# excel_file1 = r"C:\Users\ANANYA ROHATGI\OneDrive\Desktop\teamsbot\merged_file_correct.xlsx"
# excel_file2 = r"C:\Users\ANANYA ROHATGI\OneDrive\Desktop\teamsbot\Key Metrics1.xlsx"

# # Read all sheets from both Excel files
# dfs1 = pd.read_excel(excel_file1, sheet_name=None)
# dfs2 = pd.read_excel(excel_file2, sheet_name=None)

# smart_dfs1 = [SmartDataframe(df, config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True}) for df in dfs1.values()]
# smart_dfs2 = [SmartDataframe(df, config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True}) for df in dfs2.values()]

# # Combine all DataFrames into SmartDatalake
# data_lake = SmartDatalake(smart_dfs1 + smart_dfs2, config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True})

# class MyBot(ActivityHandler):
#     async def on_message_activity(self, turn_context: TurnContext):
#         user_query = turn_context.activity.text
#         try:
#             response = data_lake.chat(user_query)

#             if isinstance(response, str):
#                 await turn_context.send_activity(response)

#             elif isinstance(response, pd.DataFrame):
#                 df_string = response.to_string(index=False)
#                 await turn_context.send_activity(f"Here are the results:\n```\n{df_string}\n```")

#             elif isinstance(response, dict) or isinstance(response, list):
#                 await turn_context.send_activity(str(response))

#             elif isinstance(response, numbers.Number):  # Handles both int and float
#                 await turn_context.send_activity(str(response))

#             elif isinstance(response, plt.Figure):  # If response is a matplotlib Figure
#                 image_attachment = self.convert_figure_to_attachment(response)
#                 reply = Activity(
#                     type="message",
#                     attachments=[image_attachment]
#                 )
#                 await turn_context.send_activity(reply)

#             elif isinstance(response, str) and response.startswith("exports/charts/"):
#                 base64_image = self.convert_image_to_base64(response)
#                 if base64_image:
#                     image_attachment = Attachment(
#                         content_type="image/png",
#                         content_url=f"data:image/png;base64,{base64_image}",
#                         name="chart.png"
#                     )
#                     reply = Activity(
#                         type="message",
#                         attachments=[image_attachment]
#                     )
#                     await turn_context.send_activity(reply)
#                 else:
#                     await turn_context.send_activity("Image not found or failed to load.")

#             elif isinstance(response, Exception):
#                 await turn_context.send_activity(f"An error occurred: {str(response)}")

#             else:
#                 await turn_context.send_activity(f"Unexpected response type: {type(response).__name__}. Content: {str(response)}")
                
#         except Exception as e:
#             await turn_context.send_activity(f"Error processing request: {str(e)}")

#     def convert_figure_to_attachment(self, fig):
#         """Convert a Matplotlib figure to a Base64 image and return as an attachment."""
#         img_stream = io.BytesIO()
#         fig.savefig(img_stream, format="png")  # Save figure as PNG in memory
#         img_stream.seek(0)
#         base64_str = base64.b64encode(img_stream.getvalue()).decode()
        
#         return Attachment(
#             content_type="image/png",
#             content_url=f"data:image/png;base64,{base64_str}",
#             name="chart.png"
#         )

#     def convert_image_to_base64(self, image_path):
#         """Convert an image file to Base64 encoding."""
#         try:
#             if not os.path.exists(image_path):
#                 print(f"File not found: {image_path}")  # Debugging
#                 return ""

#             with open(image_path, "rb") as img_file:
#                 return base64.b64encode(img_file.read()).decode()
#         except Exception as e:
#             print(f"Error loading image: {e}")
#             return ""

#     async def on_members_added_activity(self, members_added, turn_context: TurnContext):
#         for member_added in members_added:
#             if member_added.id != turn_context.activity.recipient.id:
#                 await turn_context.send_activity("Hello and welcome!")
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import Activity, Attachment
from pandasai import SmartDataframe, SmartDatalake
from pandasai.llm.azure_openai import AzureOpenAI
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt
import os
import numbers
from bs4 import BeautifulSoup  

# Initialize Azure OpenAI LLM
llm = AzureOpenAI(
    
)

# File paths
excel_file1 = r"C:\Users\ANANYA ROHATGI\OneDrive\Desktop\teamsbot\merged_file_correct.xlsx"
excel_file2 = r"C:\Users\ANANYA ROHATGI\OneDrive\Desktop\teamsbot\Key Metrics1.xlsx"

# Read all sheets from both Excel files
dfs1 = pd.read_excel(excel_file1, sheet_name=None)
dfs2 = pd.read_excel(excel_file2, sheet_name=None)

smart_dfs1 = [SmartDataframe(df, config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True}) for df in dfs1.values()]
smart_dfs2 = [SmartDataframe(df, config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True}) for df in dfs2.values()]

data_lake = SmartDatalake(smart_dfs1 + smart_dfs2, config={"llm": llm, "enable_cache": False, "save_charts": True, "enable_explainability": True})

class MyBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_query = turn_context.activity.text
        try:
            response = data_lake.chat(user_query)
            print(f"Response Type: {type(response)}")

            if isinstance(response, str):
                if response.startswith("exports/charts/"):
                    if os.path.exists(response):
                        base64_image = self.convert_image_to_base64(response)
                        html_chart = self.generate_html_chart(base64_image)
                        await turn_context.send_activity(html_chart)
                    else:
                        await turn_context.send_activity(f"Image file not found: {response}")
                else:
                    await turn_context.send_activity(response)
            elif isinstance(response, pd.DataFrame):
                df_string = response.to_string(index=False)
                await turn_context.send_activity(f"Here are the results:\n```\n{df_string}\n```")
            elif isinstance(response, numbers.Number):
                await turn_context.send_activity(str(response))
            elif isinstance(response, plt.Figure):
                image_attachment = self.convert_figure_to_attachment(response)
                reply = Activity(type="message", attachments=[image_attachment])
                await turn_context.send_activity(reply)
            else:
                await turn_context.send_activity(f"Unexpected response type: {type(response).__name__}")
        except Exception as e:
            await turn_context.send_activity(f"Error processing request: {str(e)}")

    def convert_figure_to_attachment(self, fig):
        """Convert a Matplotlib figure to a Base64 image and return as an attachment."""
        img_stream = io.BytesIO()
        fig.savefig(img_stream, format="png")
        img_stream.seek(0)
        base64_str = base64.b64encode(img_stream.getvalue()).decode()
        return Attachment(content_type="image/png", content_url=f"data:image/png;base64,{base64_str}", name="chart.png")

    def convert_image_to_base64(self, image_path):
        """Convert an image file to Base64 encoding."""
        try:
            if not os.path.exists(image_path):
                return ""
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        except Exception as e:
            print(f"Error loading image: {e}")
            return ""

    def generate_html_chart(self, base64_image):
        """Embed Base64 PNG into HTML for rendering."""
        html_content = f"""
        <html>
        <body>
            <h3>Generated Chart:</h3>
            <img src="data:image/png;base64,{base64_image}" alt="Chart">
        </body>
        </html>
        """
        soup = BeautifulSoup(html_content, "html.parser")
        return str(soup)

    async def on_members_added_activity(self, members_added, turn_context: TurnContext):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
