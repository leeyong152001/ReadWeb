from pypdf import PdfReader 

# creating a pdf reader object 
reader = PdfReader('example.pdf') 
  
# printing number of pages in pdf file 
# print(len(reader.pages)) 
for i in range(len(reader.pages)):
    # creating a page object 
    page = reader.pages[i] 
    
    # extracting text from page 
    with open('filetext.txt','a', encoding='utf-8') as f:
        page = page.extract_text().removeprefix('https://thuviensach.vn')
        text = " ".join(page.split())
        f.write(text)
        f.close()