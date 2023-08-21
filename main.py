import streamlit as st
import openai
import json
from graphviz import Digraph



openai.api_key = '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'  # replace with your OpenAI key
st.set_page_config(layout="wide")
@st.cache_data
def normalization(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content":
                """
                 We have developed a design system for ambient computing environments. The system basically consists of four main components: hardware modules, software modules, hardware inputs, and software inputs. For example, in the instance of a student being granted access to a studio the RFID system would be the hardware module, the UUID from the student ID card would be the software input, the access management system would be the software module and the signal from the access management system (whether access granted or refused) will be a software output.

You are a helpful AI assistant who can take in the raw description of a workflow that isn't described in the before-mentioned design system and standardize and normalize it so it is in that design system format.

Your response should be a JSON response. For instance, in the above case, it would look like this:

{
  "workflow": [
    {
      "step": 1,
      "type": "software input",
      "content": "UUID"
    },
    {
      "step": 2,
      "type": "hardware module",
      "content": "RFID Sensor"
    },
    {
      "step": 3,
      "type": "software output/input",
      "content": "Signal"
    },
    {
      "step": 4,
      "type": "software module",
      "content": "Access Management System"
    },
    {
      "step": 5,
      "type": "software output/input",
      "content": "Approval/Rejection signal"
    },
    {
      "step": 6,
      "type": "hardware module",
      "content": "Door actuator"
    },
    {
      "step": 7,
      "type": "hardware output",
      "content": "Door opened/closed"
    }
  ]
}

Here are some rules:
Keep in mind every module needs to have an input and output, meaning you can't have a module connected to a module, there has to be a signal present between them.
Also, the workflow always starts with an input signal (hardware or software) and ends with a signal (never a module).
Plus, one module cannot have more than one input and more than one output.
Finally, and most importantly the hardware and software modules and signals can only be from the following array

HARDWARE:

1. Prusa 3D Printers
2. Consumer Grade Sewing Machines
3. LulzBot TAZ 6 with 1.2 mm Nozzle
4. Universal Systems Laser-Cutters, 32 x 18 in (3)
5. Juki Industrial Sewing Machine (1) and Juki Industrial Serger (1)
6. Spray Painting Booth with Fume Hood
7. Kuka Robots, “Lucy” and “Ethel”
8. Creaform Go!Scan 3D Scanner
9. Hand Tools
10. Experimental 3D Printers (2)
11. Universal Systems Laser-Cutter, 48 x 25 in
12. 4′ X 8′ Shopbot Prsalpha CNC Router
13. Othermill CNC Mills (2)
14. Vacu-Former
15. Diwire Wire Bender
16. Other Power Tools: Drill, Foredom Rotary Hand Tool, Jigsaw, Staple Gun, Orbital Sander
17. Soldering Irons
18. PCB Shear
19. Oscilloscopes and Power Supplies
20. Multi-Meters
21. Saleae Logic Analyzer
22. Heat Guns
23. Stereo Microscope
24. SawStop 10” Table Saw
25. Laguna 18 3000 Series Vertical Band Saw
26. Disk/Belt Sander Combo
27. Bosch Sliding Compound Miter Saw
28. Delta Variable Speed Drill Press
29. Omax 2626 Waterjet Cutter
30. Baileigh Combination Shear/Brake/Roll
31. Baileigh 20-Ton Press
32. Ellis Horizontal Bandsaw
33. 16″ South Bend Vertical Bandsaw
34. Clausing Drill Press
35. Kalamazoo Belt Sanders (2)
36. TIG Welding Area
37. Tormach Module
38. Fablight
39. Sharp Manual Knee Mill
40. Stratasys Fortus 380MC 3D Printer
41. Objet260 Connex3 Multi-Material Color 3D Printer
42. Form 3 SLA Printer (4)
43. Markforged X7 3D Printer
44. Function Generators
45. Fume Extractors
46. VirtualBench
47. 36″ Canon iPF785 Large-Format Printer
48. Elmo Document Camera
49. Canon EOS 5D Mark III with 24-105mm Lens
50. Tripods and Monopods
51. Photo Backdrop with Bescor LED-700 Lighting
52. High-Resolution Scanner
53. HTC VIVE AR/VR Headset and Controllers

SOFTWARE:

1. 3D Printer Software for controlling the 3D printers
2. CNC Software for controlling the CNC machines
3. Laser-Cutter Software for controlling the laser-cutters
4. Robotics Software for controlling the robots
5. Digital Design Software for wire bending machine
6. AR/VR Software for controlling AR/VR devices
7. Digital Electronic Measurement Software used with Oscilloscopes and Logic Analyzer
8. VirtualBench Software for controlling circuits in VirtualBench
9. 3D Scanning Software for 3D Scanners
10. Image Processing Software for Cameras and Scanners
11. Welding Software for controlling the TIG Welding area.
"""},
            {"role": "user", "content": text},
        ]
    )
    response_content = response["choices"][0]["message"]["content"]
    # response_content_dict = json.loads(response_content)
    return response_content

col1, col2 = st.columns([1,1])

with col1:
    st.text("""

HARDWARE:

1. Prusa 3D Printers
2. Consumer Grade Sewing Machines
3. LulzBot TAZ 6 with 1.2 mm Nozzle
4. Universal Systems Laser-Cutters, 32 x 18 in (3)
5. Juki Industrial Sewing Machine (1) and Juki Industrial Serger (1)
6. Spray Painting Booth with Fume Hood
7. Kuka Robots, “Lucy” and “Ethel”
8. Creaform Go!Scan 3D Scanner
9. Hand Tools
10. Experimental 3D Printers (2)
11. Universal Systems Laser-Cutter, 48 x 25 in
12. 4′ X 8′ Shopbot Prsalpha CNC Router
13. Othermill CNC Mills (2)
14. Vacu-Former
15. Diwire Wire Bender
16. Other Power Tools: Drill, Foredom Rotary Hand Tool, Jigsaw, Staple Gun, Orbital Sander
17. Soldering Irons
18. PCB Shear
19. Oscilloscopes and Power Supplies
20. Multi-Meters
21. Saleae Logic Analyzer
22. Heat Guns
23. Stereo Microscope
24. SawStop 10” Table Saw
25. Laguna 18 3000 Series Vertical Band Saw
26. Disk/Belt Sander Combo
27. Bosch Sliding Compound Miter Saw
28. Delta Variable Speed Drill Press
29. Omax 2626 Waterjet Cutter
30. Baileigh Combination Shear/Brake/Roll
31. Baileigh 20-Ton Press
32. Ellis Horizontal Bandsaw
33. 16″ South Bend Vertical Bandsaw
34. Clausing Drill Press
35. Kalamazoo Belt Sanders (2)
36. TIG Welding Area
37. Tormach Module
38. Fablight
39. Sharp Manual Knee Mill
40. Stratasys Fortus 380MC 3D Printer
41. Objet260 Connex3 Multi-Material Color 3D Printer
42. Form 3 SLA Printer (4)
43. Markforged X7 3D Printer
44. Function Generators
45. Fume Extractors
46. VirtualBench
47. 36″ Canon iPF785 Large-Format Printer
48. Elmo Document Camera
49. Canon EOS 5D Mark III with 24-105mm Lens
50. Tripods and Monopods
51. Photo Backdrop with Bescor LED-700 Lighting
52. High-Resolution Scanner
53. HTC VIVE AR/VR Headset and Controllers

SOFTWARE:

1. 3D Printer Software for controlling the 3D printers
2. CNC Software for controlling the CNC machines
3. Laser-Cutter Software for controlling the laser-cutters
4. Robotics Software for controlling the robots
5. Digital Design Software for wire bending machine
6. AR/VR Software for controlling AR/VR devices
7. Digital Electronic Measurement Software used with Oscilloscopes and Logic Analyzer
8. VirtualBench Software for controlling circuits in VirtualBench
9. 3D Scanning Software for 3D Scanners
10. Image Processing Software for Cameras and Scanners
11. Welding Software for controlling the TIG Welding area.
""")
with col2:
    text = st.text_area("Enter raw description here:")
    if st.button("Normalize"):
        st.json(f"{normalization(text)}")
        print(normalization(text))
        workflow_data = json.loads(normalization(text))["workflow"]

        dot = Digraph(comment='Workflow')
        dot.attr('node', shape='rectangle')

        for step in workflow_data:
            if 'software module' in step['type']:
                dot.attr('node', fillcolor='#03a1fc', style='filled')
            elif 'hardware module' in step['type']:
                dot.attr('node', fillcolor='#ab4711', style='filled')
            else:
                dot.attr('node', fillcolor='white', style='filled')
            dot.node(step['content'])

        for i in range(len(workflow_data) - 1):
            dot.edge(workflow_data[i]['content'], workflow_data[i + 1]['content'])

        st.graphviz_chart(dot.source)
# Displays the returned value from the function as JSON in Streamlit.