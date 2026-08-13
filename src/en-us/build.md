# Hardware & Build

## 1. Basic Requirements

The following are supplementary requirements for Hardware & Build.

### Applications

- Bambu Studio
- RD Works V8

### Online Accounts

- Email address (@gmail.com or @outlook.com recommended)
- Bambu Studio — [https://bambulab.cn/](https://bambulab.cn/)
- Onshape — [https://www.onshape.com/](https://www.onshape.com/)
- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/)

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

### Bambu Studio

Bambu Studio is the 3D-printing solution adopted by our team.

**Registration:**

1. Open [https://bambulab.cn/](https://bambulab.cn/) and register an account with a phone number or another method.

**Software installation and configuration:**

1. Open [https://bambulab.cn/en/download/studio](https://bambulab.cn/en/download/studio)
2. Download and install the appropriate version for your platform.

**Important notes:**

- On Windows, you may change the installation directory, as long as the path ends with `..\Bambu Studio\`. During installation, check "Open .3mf files with Bambu Studio", "Open .stl files with Bambu Studio", and "Open .step/.stp files with Bambu Studio".
- On macOS, drag `BambuStudio.app` into the Applications folder.
- Launch Bambu Studio. Select "Mainland China" as the login region. Select at least the **Bambu Lab P1S** and **Bambu Lab P2S** printers; keep materials at default settings. Check "Install Bambu Network plugin".
- Log in to your Bambu account with a phone number or another method.

### RD Works V8

> [!danger] **Note:** Installing this program on macOS is strongly discouraged — it would require virtual machine support such as Parallels Desktop, VMware Fusion, or CrossOver.

RD Works V8 is the companion driver software for our laser cutter.

**Software installation and configuration:**

1. Obtain the `RDWorksV8Setup.exe` installer from an administrator or mentor, open it, and click "Install".
2. You may change the installation path by checking "manually locate the installation path".
3. Connect your computer to the laser cutter and click "Install USB driver".
4. Keep all other options at their defaults.

---

## 3. Supplies Overview

### Common Tools

> [!danger] Before using any hand tool, always check that it is in good condition (e.g., handle not loose, jaws not chipped), and wear protective gloves or goggles as needed.

> [!info] Only the most frequently used tools are covered here. All other tools are compiled into the *Tool List* appendix, which will keep growing over time.

#### Hex Key (Allen Wrench)

An L-shaped or T-shaped tool with a regular hexagonal cross-section, used to turn socket-head screws. Insert either end fully into the hexagonal recess of the screw head; turn clockwise to tighten and counterclockwise to loosen. T-handle wrenches provide greater leverage or reach in deep bores.

> [!info] The sizes we use most often are M3 and M4 — always keep them at hand.

#### Socket

A cylindrical fastening tool with a hexagonal bore that fits over a nut or bolt head. Place the socket vertically onto the nut and rotate it via the handle. Its advantages include a large contact area (less slippage) and suitability for tight spaces where ordinary wrenches cannot turn.

#### Adjustable Wrench

A general-purpose wrench whose jaw opening can be adjusted within a certain range, fitting hex nuts of various sizes. Turn the worm gear to adjust the opening until it grips the nut flats. Always make sure the fixed jaw bears the main thrust or tension — i.e., apply force toward the fixed-jaw side — to prevent damage or slippage.

#### Flat-Nose Pliers

A gripping tool with flat jaws, usually serrated on the inside to increase friction. Use them for bending sheet metal, holding small parts, or providing auxiliary pull during assembly.

#### Needle-Nose Pliers

Pliers with long, slender, conical jaws suited to tight workspaces. Commonly used to grip tiny parts, bend fine wires, or retrieve foreign objects from dense circuits or structures. The base of the jaws usually has a cutting edge, doubling as wire cutters.

#### Wire Stripper

A tool specifically designed to remove wire insulation without damaging the conductor. Choose the notch matching the wire gauge, place the wire in the notch, squeeze the handles, and gently twist while pulling outward to strip the insulation.

#### Claw Hammer

A tool used to strike objects to move or deform them. One face is flat for driving; the other end is a V-shaped claw for pulling nails. Grip the end of the handle for maximum torque. Keep the hammer face parallel to the target surface when striking to prevent glancing blows.

#### Tape Measure

A flexible metal tape with a spring retraction mechanism, used for measuring longer distances or non-linear dimensions. Pull out the tape, hook the end claw onto an edge or butt it against a reference surface, read the graduations, and retract the tape with the locking button or the auto-return spring. Note that the hook has slight intentional play, which compensates for its thickness so that inside and outside measurements read identically.

#### Vernier Caliper

A vernier caliper consists of a main scale (A) and a vernier scale (B) that slides along it.

- **Principle**: A vernier caliper exploits the fixed small difference between the unit graduations of the main scale (1 mm) and those of the vernier scale to improve measurement precision. Common vernier calipers come in 10-division, 20-division, and 50-division varieties.
- **Reading**: Read the main scale first — locate the zero line of the vernier scale relative to the main scale graduations. Then read the vernier scale — find which graduation line aligns exactly with a main scale line. Combine the two readings to obtain the measured length.
- **Usage**: When the two jaws of the outside (inside) measuring faces touch, the zero line of the vernier scale aligns with the zero line of the main scale. Clamp (or seat) the object between the jaws and combine the main and vernier readings to obtain the object's length.

#### Micrometer

A micrometer consists of an anvil (A) and a fixed sleeve scale (B) mounted on a frame (C). The thimble scale (E), thimble (D), and ratchet stop (D') are connected to the spindle (F), which threads through B via a precision screw.

- **Principle**: When the thimble D rotates one full turn, the spindle F advances or retracts one pitch along the axis. The fixed sleeve scale B has a pitch of 0.5 mm, and the thimble scale E has 50 equal divisions — so each thimble division corresponds to 0.01 mm of spindle travel. A micrometer measures accurately to 0.01 mm.
- **Reading**: Read scale B first, noting whether the half-millimeter line is exposed. Then read scale E, where each division corresponds to 0.01 mm. Combine the readings from B and E to obtain the measured length.
- **Usage**: To measure small dimensions, first bring F into contact with A and align the left edge of E with the zero line of B. Place the object between F and A, rotate D until F approaches the object, then switch to the ratchet D' and stop when you hear the "click". Then take the reading.

### Common Materials

#### General Materials

Available from a wide range of sources:

- Screws and nuts of various sizes
- Hexagonal standoffs
- Timing pulleys
- Bearings

> [!warning] Shafts are excluded from general materials: shaft requirements are project-specific — purchase them separately as needed.

#### Specialized Materials

Official REV and goBILDA products, plus Zhou Yu as a specialized extrusion supplier.

#### Material Characteristics

| Brand | Characteristics |
|------|------|
| **REV** | Relatively old but core. The three main control system modules (Driver Hub, Control Hub, Expansion Hub) are REV products. Structural parts include various aluminum extrusions (used less frequently); extrusions can serve as small limit brackets or fix non-unit-displacement structures. Extrusions take M3 button-head screws only; 6 mm REX shafts; gears and chains; 72:1 transverse motors and 40:1 motors are the most usable. |
| **goBILDA & Zhou Yu** | C-channels, square or thin beams, 8 mm REX shafts, a wide range of modular connectors with well-rounded functionality. Primarily M4 screws (10 mm official); motors are mostly 5203 series. Suitable for direct-drive motor kits. |

**REV details:**

- **Core control modules**: The Driver Hub, Controller Hub (Control Hub), and Expansion Hub are REV products.
- **Structural parts**: Mostly aluminum extrusion, rarely used at present — suitable for small limit brackets and fixing non-unit-displacement structures.
- **Special screws**: REV extrusions use M3 button-head (socket) screws, which seat inside the extrusion slots — almost exclusive to REV extrusion.
- **Shaft spec**: REV uses 6 mm REX shafts — a REV-specific size.
- **Motors**: REV offers a 72:1 transverse motor (officially the Core Hex Motor, 90° orientation, no built-in output shaft) and a 40:1 standard motor (officially the HD Hex Motor). The 72:1 transverse motor enables special mounting solutions, but its design is dated and hard to find compatible partners for nowadays.
- **Gears and chains**: REV also supplies them, but goBILDA products are generally preferred.

**goBILDA details:**

- **C-channels**: Two kinds — square beams and thin beams. Square beams suit large frame structures such as chassis; thin beams suit span connections.
- **Connectors**: A wide range of standardized connectors, highly modular, with well-rounded compatibility with both its own and REV materials.
- **Screw spec**: Primarily M4 screws; the official pairing is M4×10 mm button-head screws.
- **Shaft spec**: 8 mm REX shafts.
- **Motors**: Commonly the 5203 series, suited to standard direct drive. Thanks to the strength of the 8 mm REX shaft and its motor mounting style, goBILDA is the kit of choice for direct motor drive.

**Zhou Yu details:**

> [!warning] Most goBILDA equivalents can be found at Zhou Yu, with some differences. Prefer official goBILDA hardware whenever possible; Zhou Yu is cheaper but may have quality issues.

- Most materials have a corresponding goBILDA-style counterpart at Zhou Yu.
- Zhou Yu also makes some special parts designed for domestic needs; some have no goBILDA equivalent. If you find an ingenious Zhou Yu part, you can buy it for testing.
- Price-wise, Zhou Yu is the cheapest of the three suppliers, but workmanship is slightly below goBILDA.

#### 3D Printing Filaments

| Type | Print temperature (approx.) | Description |
|------|------|------|
| PLA | 220°C | Standard base plastic filament |
| PETG-CF | 240+°C | Carbon-fiber-reinforced filament |

Purchase official Bambu Lab or SUNLU filaments for consistent quality.

**Shrinkage:**

- Normally, PLA shrinkage is not a concern.
- When printing bushings, diameter shrinkage of about 5% can occur — measure it based on the printed geometry.
- PETG-CF shrinkage fluctuates significantly with time, temperature, and batch. Before use, print a simple test piece matching your part's geometry to measure shrinkage.

#### Laser Cutting Materials

| Material | Characteristics | Use case |
|------|------|------|
| Acrylic sheet | High strength | Large-span load-bearing panels |
| PP sheet | High toughness | Protective panels; needs more attachment points; withstands direct impact |
| Plywood | Low cost | Prone to warping; special cases only |

> [!info] Material properties are fixed here. Laser cutting parameters (power, speed, etc.) go in the appendix, which is updated continuously.

#### Cables

**Power cables:**

- Battery-to-Hub cable (depending on design, the battery may connect directly to either the Control Hub or the Expansion Hub)
- Con-to-EXP cable
- Switches that come with their own wiring
- Motor power cables: goBILDA motor power connectors are incompatible with the Hub — cut off the original connector and remake the head with a wire ferrule.

**Data cables (motor encoder cables):**

- For goBILDA, the connector and pinout differ from the Hub (yellow and white wires are swapped) — be especially careful when making them.
- I2C sensor cables: no special requirements.
- Con and EXP data cables.
- Servo extension cables: watch the orientation.

**Host data cables:**

- Hub-to-computer connection: use a USB-A to USB-C cable for the Control Hub, and a mini-USB cable for the Expansion Hub.
- Others: USB-A to USB-C, USB-A to mini-USB, USB-C to mini-USB, and other conversion cables.
- Ethernet cable (usable as an auxiliary network connection — not required).
- Controller data cable (USB-A to micro-USB).

**Infrastructure (treated as consumables):**

- Wi-Fi, monitoring, network cables, power strips, and other infrastructure are managed as consumables — replenish them in time.

---

## 4. Workflow

1. **Parts procurement**
2. **Custom part fabrication**
   - 3D-printed parts
   - Laser-cut sheet processing
3. **Hardware assembly**
4. **Wiring**
5. **Robot Configuration authoring** (in coordination with Programming)
6. **Connecting the Driver Station to the Robot Controller** (in coordination with Programming)

### Hardware Assembly

#### Assembly Order

> [!warning] The conventional hand-build approach builds the chassis first and stacks upward. But in competition robots, we have CAD models — that order easily leads to massive rework due to part occlusion.

- Adjust the assembly order according to occlusion: **install parts that will be blocked by motors or electronics first**, then install the blocking components.
- Example: finish installing everything around a motor before mounting the motor itself.

#### Part Usage Notes

- On shafts, avoid prioritizing parts with set screws — set screws damage shafts.
- Do not over-tighten screws.
- More part usage rules will be added over time.

#### Leave Room for Repairs

- Never take shortcuts when assembling: don't hide screws and nuts in hard-to-reach spots.
- Everything must follow the "easy to repair" principle — if a breakdown requires disassembling the entire robot, your competition is over.

#### ESD Protection

- Dry weather generates static electricity, which can cause disconnections and inaccurate sensor readings.
- Countermeasures: add a grounding wire to the robot to drain static to the floor; wrap IMU and other sensors in tin foil for electrostatic shielding.

#### Cable Management

- Telescoping structures with linear slides must be wrapped in cable sleeving to prevent wires from flying loose, jamming the slides, or being torn off.
- Cable management is the most skill-intensive part of assembly — take it seriously.

### Wiring

#### Connecting the Control Hub and Expansion Hub

- **Power**: male connector to female connector.
- **Data**: connect via RS-485 ports using 3-pin cables. Each side has 2 RS-485 ports — pick one on each side; they do not need to correspond to fixed positions.

> [!warning] All official connectors are keyed — the design prevents wrong insertion but not stubbornness. If a connector will not seat, check the orientation before applying any force.

#### Connecting the Driver Station and Robot Controller

Network connection is required knowledge for both Hardware and Programming — reuse the content from the Programming section.

#### Robot Configuration Authoring

Writing the configuration file is a joint Hardware/Programming task — see the Programming section.

---

## 5. Hardware & Build Starter

### Installing and Configuring Bambu Studio

Download and install, clicking "Next" throughout. Note the installation location — a folder is created automatically.

**Notes:**

- All checkboxes must be checked
- When launching, follow the registration guide and select Mainland China
- Select only the P1S and P2S printers
- Keep material selections at default
- Install the network plugin
- Log in/register from the top-left corner (phone number or third-party login)

### Exporting Models from Onshape

1. Open the model, select the target part — its position in the instance list on the left will be highlighted in the bottom-left corner.
2. Right-click the part and choose to switch to the corresponding instance workspace to enter the Part Studio.
3. Right-click the part in the parts list and choose Export.
   - Note: the Export option only appears if you have edit access to the document.
4. Set the format to STEP, rename the file as needed, and leave the rest at defaults.

### Importing and Arranging in Bambu Studio

- Create a new project in Bambu Studio, click the "Import" button at the top to import the STEP file, and confirm the import options with defaults.
- If the part lands in an unwanted position, deselect everything, right-click the build plate, and choose "Auto Arrange" or "Auto Orient".
- Manual adjustment: select the part, hold the left button to drag and move; use the Rotate button to rotate via relative or absolute modes.
- Interaction difference: by default, Bambu Studio matches Onshape — left-drag rotates the view and right-drag pans; you can adjust the view controls in settings if preferred. Left-dragging a selected part moves the part directly.

### Print Parameter Configuration

**Printer and filament selection:**

| Printer | Nozzle | Filament |
|--------|------|------|
| P1S (stock nozzle) | 0.4 mm | PLA Basic |
| P1S (nozzle replaced, dedicated to carbon filament) | 0.6 mm | PETG-CF |
| P2S (both units) | 0.4 mm | PLA Basic |

**Process presets by part type:**

| Type | Preset |
|------|------|
| Decorative parts | Bambu Studio defaults |
| Non-load-bearing structural parts | Team standard configuration |
| Load-bearing structural parts | Team standard configuration (high strength) |

> [!info] These presets are our team's standard configurations — modify them if you have special requirements.

**Multiple parts on one plate:**

- Need multiple identical parts: select the part, right-click, choose "Clone".
- Need different parts: click the "Import" button again to import.

### Connecting to 3D Printers

- Go to the "Device" tab, enable LAN mode, and the printer will be auto-discovered on the LAN (enabling LAN mode may log you out — you can ignore the prompt).
- If the target printer cannot be found: first confirm the printer has LAN mode enabled; if still invisible, bind it manually via IP + access code. The IP is under Settings > WiFi on the printer; the access code is shown at the login avatar position after enabling LAN mode.
- After slicing, review in the "Preview" tab. Before printing, send the sliced preview to the current modeling or build lead for confirmation.

### Print Settings

**P2S printers:**

- Enable time-lapse before printing.
- Auto bed leveling must be enabled.
- Select the loaded filament and target printer.

**P1S printers:**

- Time-lapse can stay off.
- Auto bed leveling and dynamic flow calibration must both be set to automatic.

### Print Failure Handling

- **P2S**: With AI spaghetti detection — on spaghetti failure (filament flying loose), the printer stops automatically and notifies the logged-in account. After clearing the failed job, the printer restarts automatically.
- **P1S**: No automatic spaghetti detection — monitor the print in real time. If spaghetti occurs, stop the print manually; find the failed job in the history under the cache folder on the left and clean it up.

### Installing and Configuring RD Works V8

**Installation:**

1. Get the exe installer from an administrator or mentor and choose Install
2. Check "manually locate the installation path" to change the location
3. Keep other options at their defaults
4. Once connected to the laser cutter, choose to install the USB driver
5. Close and reopen the software to finish
