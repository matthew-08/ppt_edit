import collections 
import collections.abc
from pptx import Presentation


prs = Presentation('example.pptx')


text_runs = []

for slide in prs.slides:
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for paragraph in shape.text_frame.paragraphs:
            temp = dict({slide.slide_id: []})
            for run in paragraph.runs:
                temp[slide.slide_id].append(run.text)
                text_runs.append(temp)
for k in text_runs:
    print(k.items())
prs.save('test.pptx')