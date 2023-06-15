# CDC API Project

In this project we use the CDC's Wonder API (https://wonder.cdc.gov/wonder/help/WONDER-API.html) to obtain cancer death data in the date range between 1999 and 2013. Requests to the API are written in xml, and documentation on how to write one's own resquest was difficultto find. Therefore, this data in particular was chosen to follow along with the example request and response given on their website ("1st Example Request").

### File Contents
The The document **cdc_wonder_api_requests.py** brings in the **req.xml** file and makes a request of the API per the structure of req.xml. The response is saved as **response.xml**. Responses are, of course, in xml format. The data is structured hierarchically: rows contain cells, which contain values. Some care is needed when parsing this into your language of choice. Year is contained right along with other values so that they don't get their own column if one is not careful. Additionally, every five rows contains a subtotal row. **xml_parser.py** does this work of parsing the response file. We intentionally discarded the subtotal rows to simplify the work of parsing, and pickled and saved the resulting dataframe as **my_df.pkl**

![example_response](response_example.png)

With the technical hurdles of data acquisition overcome, we performed our exploration and analaysis in a series of jupyter notebooks.