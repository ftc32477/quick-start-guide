# 3D Modeling & Design

## 1. Basic Requirements

The following are supplementary requirements for 3D Modeling & Design.

### Applications

- Web browser (Chrome, Edge, or Safari)
- LocalSend
- Onshape FTC parts library — [https://ftconshape.com/](https://ftconshape.com/) (maintained by FIRST and PTC; email FIRST@ptc.com to be added to the shared folder)
- FTC Insert Tool parts library plugin — [https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba](https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba) (install from the Onshape App Store: Subscribe → Get for Free)

### Online Accounts

- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/) (free, application required)

---

## 2. Environment Setup

The following environment must be configured before you begin. If you have any questions, please consult an administrator.

### Web Browser

Bookmark the following additional websites:

| Name | URL |
|------|------|
| goBILDA | https://www.gobilda.com/ |
| REV Robotics | https://www.revrobotics.com/ |
| CycleZLab | https://www.cyclezlab.com/ |
| Onshape for Education | https://www.onshape.com/en/education/ |

### Onshape Account Registration

Onshape is the cloud-based CAD platform adopted by our team. Compared with industrial modeling software such as SolidWorks, Onshape is light on system resources, makes sharing projects across devices easy, is beginner-friendly, and has official FIRST support—while remaining fully functional, it is ideal for learning CAD modeling and working on projects.

**Registration:**

1. Open [https://www.onshape.com/en/education/](https://www.onshape.com/en/education/) and sign up for an Education account
2. Enter your first name, last name, and email address

> [!warning] Do not use QQ or other Chinese domestic email providers—verification emails may never arrive. Use @gmail.com or @outlook.com instead.

3. On the next screen, select your role "Student", school level "Grade School / K-12 (Ages <18)", and date of birth, then click Next
4. Fill in the following information:
   - School name: BEIJING NATIONAL DAY EXPERIMENTAL SCHOOL
   - School website: [https://sysyzx.bjhdedu.cn/](https://sysyzx.bjhdedu.cn/)
   - Expected graduation year
   - Reason for registering: I am a member of FTC Team 32477, and I registered this account to use the team's modeling tools. (fill this in if you are unsure what to write)
   - Check all three agreement boxes to complete registration
5. Check your email for the confirmation message

> [!info] After registering, give your account name to an administrator so they can add you to the team's shared folder.

**Common issues:**

- reCAPTCHA error on the final step: the human-verification service did not respond. Try switching networks and make sure the reCAPTCHA service is reachable.
- No verification email received: if you have waited more than 3 minutes, try a different email address (Outlook or Gmail—not QQ)

### Onshape Preferences Setup

1. Enter the workspace, click the account icon in the top-right corner, and select "My account", the first item in the dropdown menu
2. Select "Preferences", the third item from the top of the menu, change the first language option to "Simplified Chinese", then click Save
3. In the same menu, change the units option to metric (millimeters are the default length unit in the team's working environment)

> [!info] These changes only apply to documents created afterwards; existing documents keep their original units.

4. Update your profile as you prefer

### Onshape Plugins

Thanks to its cloud-based nature, Onshape has a rich ecosystem of shared plugins, available through the Onshape App Store, third-party plugin websites, and sharing between users.

Plugins commonly used by the team include (examples only):

- **Onshape FTC parts library** (core; see "1. Basic Requirements")
- **Lighten** (custom feature that slims down parts to make them lighter)
- **Spur gear** (custom feature, gear generator)
- **HTD Pulley Generator** (derived from another document, timing belt pulley generator)

---

## 3. Modeling Essentials

### Part Design and Assembly

When performing 3D modeling in Onshape, pay special attention to the following:

- **Dimensional accuracy**: ensure all dimensions in the model match the physical parts
- **Assembly mates**: set up part-to-part mates (Mates and Mate Connectors) properly
- **Interference check**: run interference checks after assembly
- **Part naming**: name parts and assemblies according to unified conventions

### Project Documents and Workspace

When working on team projects, create documents in the team's shared folder so that other members can access them. If you have not been added yet, contact an administrator to add you to the shared folder.

1. In your personal workspace, select "Shared with me" in the left menu and open the "32477" folder. There you can create a new document or open an existing team document (a document is a project)
2. To create a new project: click the blue Create button in the top-left corner, select "Document", and wait for the document to be created and opened

Once in the workspace, you will see "Part Studio" and "Assembly" tabs at the bottom (click the plus sign to the right of the tabs to create new ones):

- **Part Studio**: the area where individual parts are modeled (corresponding to the sketch and part stages of a CAD workflow); parts are created through sketch constraints
- **Assembly**: the area where parts made in Part Studios, or ready-made parts from libraries, are assembled (corresponding to the assembly stage of a CAD workflow)

A document can contain any number of Assemblies and Part Studios. For ease of editing and management, keep the following in mind: model only one part per Part Studio when possible; assemble the robot by subsystems, then bring everything together in one top-level assembly.

### Basic Modeling Workflow

As an introductory guide, this section covers only the most basic Onshape operations and workflows.

#### Sketching

In a Part Studio, create a sketch, select a plane, draw the outline with sketch tools such as lines, rectangles, and circles, then fix the geometry with dimensions and geometric constraints (e.g., horizontal, vertical, tangent). Aim for a fully constrained sketch so that subsequent feature operations are reliable.

#### Creating Parts

Once the sketch is complete, use feature tools such as extrude, revolve, and sweep to turn the 2D profile into a 3D solid, then refine the part with holes, chamfers, and fillets. All features are recorded in the feature list in order and can be rolled back and edited at any time.

#### Assembling Parts

In an Assembly, insert parts made in Part Studios or ready-made parts from libraries, and connect them with Mates and Mate Connectors. After assembling, check that the motion is smooth and that there are no interferences.

#### Using Tools

Onshape provides analysis tools such as measure, section view, and mass properties, so you can check dimensions and weight at any time while modeling. The right-click menu also offers shortcuts such as hide, isolate, and rename.

### Model Strength and Design Tips

The strength of 3D-printed parts depends on the material and the geometry. Here are some commonly used structural design concepts:

- **Core structural parts** (e.g., beams, structural plates): print in PETG-CF when possible (see the Hardware & Build chapter for parameters), with a thickness of at least 4 mm
- **Guide parts** (e.g., ball tracks, structural stops): PLA is fine, with a wall thickness of at least 2 mm
- **Protective decorative parts** (e.g., side panels): wall thickness of at least 1.5 mm
- For brittle sheet materials such as acrylic, avoid dense hole patterns (hole spacing less than 3 mm); load-bearing connections between structures should be at least 7 mm wide
- Avoid sharp corners wherever possible; round them off with fillets to prevent stress concentrations that can cause cracking

> [!info] The figures above are for reference only; actual parameters must be tuned and validated on physical parts.

### Design Strategy and Season Planning

- When designing the robot, break the game tasks into small items, design the structures for each item separately, and then combine them
- Before formal modeling, consult your teammates on the design and base it on the team's scoring strategy
- After completing the whole-robot design, consider the actual assembly process: leave assembly access for hard-to-reach screws and reserve space for cable routing
- Consider modular structures to make later repairs and optimization easier
- For the final version, aim for a unified structure and cut unnecessary small parts to improve overall strength and reduce weight

**Season planning:**

- On the schedule: the first design iteration can be rough, but it must be finished and built as soon as possible to leave time for software debugging and Driver practice, and to test the structure physically for iterative optimization. Before qualifiers, a competition-ready robot should go through at least 3 iterations (reference)
- Keep an eye on teams abroad. The FTC community has events like "Robot in 30 Hours Reveal | FTC" where teams may share their new season designs at any time. You can also reference designs from FRC and VEX teams

### Onshape Learning Resources

As a professional modeling platform, Onshape offers complete official learning resources: [https://learn.onshape.com/](https://learn.onshape.com/). There are also many tutorials on video platforms such as Bilibili and YouTube.

- Because CAD software follows similar workflows (sketch, part, assembly), tutorials for other software such as SolidWorks and Autodesk Fusion are equally valuable—they help develop spatial awareness of parts and familiarity with modeling workflows
- Remember that practice matters more than theory: find some models on Bilibili to model along with; try to model on your own first and only check the tutorial if you get stuck. In daily life, observe and think about how small structures are modeled
- For FTC, study the excellent designs of other teams: most strong teams have their own websites and open-source their designs. Search for an FTC team number on YouTube or Google to find their official site, or browse other teams' models on sites such as CycleZLab

> [!info] If you have questions, ask a modeling veteran or search online.

### Common FTC Parts Libraries

Commonly used FTC parts suppliers and resource platforms:

- **goBILDA**: provides a complete range of FTC structural components
- **REV Robotics**: provides control system modules and structural components
- **CycleZLab**: a FIRST robotics community platform (archive of CAD, code, and build logs)

### Design Standards

- Use metric units (mm)
- Leave appropriate clearance for all 3D-printed parts (0.2–0.3 mm recommended)
- Export formats: STEP files for machining, STL files for 3D printing, and 3MF files for slicing
