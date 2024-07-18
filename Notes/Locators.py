# Website: https://bootswatch.com/default/\

# This is only here to get rid of warning: 'page' is not defined
page = 0

# <button type="button" class="btn btn-primary">Default button</button>
page.get_by_role('button', name="Default button")

# <h2>Heading 2</h2>
page.get_by_role('heading', name="Heading 2")

# <div class="form-check">
#     <input class="form-check-input" type="radio" name="optionsRadios" id="optionsRadios2" value="option2">
#     <label class="form-check-label" for="optionsRadios2">
#         Option two can be something else and selecting it will deselect option one
#     </label>
# </div>
page.get_by_role('radio', name="Option two can be something else and selecting it will deselect option one")

# <div class="form-check">
#     <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
#     <label class="form-check-label" for="flexCheckDefault">
#         Default checkbox
#     </label>
# </div>
page.get_by_role('checkbox', name="Default checkbox")

# <div>
#     <label for="exampleInputEmail1" class="form-label mt-4">Email address</label>
#     <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
#     <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
# </div>
page.get_by_label("Email Address")
page.get_by_placeholder("Enter email")

# <div>
#     <label for="exampleTextarea" class="form-label mt-4">Example textarea</label>
#     <textarea class="form-control" id="exampleTextarea" rows="3"></textarea>
# </div>
page.get_by_label("Example textarea")

# <h3>
#     Heading
#     <small class="text-body-secondary">with faded secondary text</small>
# </h3>
page.get_by_text("with faded secondary text")

# <p>
#   Nullam quis risus eget 
#   <a href="#">urna mollis ornare </a> 
#   vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.
# </p>

# exact default = False
page.get_by_text("vel eu leo", exact=False)

# <p>
#     An abbreviation of the word attribute is 
#     <abbr title="attribute">attr</abbr>
#     .
# </p>
page.get_by_text("attr", exact=True)
page.get_by_title("attribute")

# <figcaption class="blockquote-footer">
#     Someone famous in <cite title="Source Title">Source Title</cite>
# </figcaption>
page.get_by_title("Source Title")


# -------------------------------- CSS Selectors -------------------------------- #


# Just like selenium

# <button type="button" class="btn btn-outline-success">Success</button>
page.locator("button.btn-outline-success")

# <button id="btnGroupDrop1" type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></button>
page.locator("button#btnGroupDrop1")

# <input type="text" readonly="" class="form-control-plaintext" id="staticEmail" value="email@example.com">
page.locator("input[readonly]")

# <input type="text" value="correct value" class="form-control is-valid" id="inputValid">
page.locator("input[value='correct value']")

# <div class="bs-component">
#               <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
#                 <div class="container-fluid">
#                   <a class="navbar-brand" href="#">Navbar</a>
#                   <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
#                     <span class="navbar-toggler-icon"></span>
#                   </button>

#                   <div class="collapse navbar-collapse" id="navbarColor02">
#                     <ul class="navbar-nav me-auto">
#                       <li class="nav-item">
#                         <a class="nav-link active" href="#">Home
#                           <span class="visually-hidden">(current)</span>
#                         </a>
#                       </li>
#                       <li class="nav-item">
#                         <a class="nav-link" href="#">Features</a>
#                       </li>
#                       <li class="nav-item">
#                         <a class="nav-link" href="#">Pricing</a>
#                       </li>
#                       <li class="nav-item">
#                         <a class="nav-link" href="#">About</a>
#                       </li>
#                       <li class="nav-item dropdown">
#                         <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Dropdown</a>
#                         <div class="dropdown-menu">
#                           <a class="dropdown-item" href="#">Action</a>
#                           <a class="dropdown-item" href="#">Another action</a>
#                           <a class="dropdown-item" href="#">Something else here</a>
#                           <div class="dropdown-divider"></div>
#                           <a class="dropdown-item" href="#">Separated link</a>
#                         </div>
#                       </li>
#                     </ul>
#                     <form class="d-flex">
#                       <input class="form-control me-sm-2" type="search" placeholder="Search">
#                       <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
#                     </form>
#                   </div>
#                 </div>
#               </nav>
#             <button class="source-button btn btn-primary btn-xs" type="button" tabindex="0"><i class="bi bi-code"></i></button>
# </div>
page.locator("nav.bg-dark a.nav-link.active")

# <div class="bs-component">
#               <ul class="list-group">
#                 <li class="list-group-item d-flex justify-content-between align-items-center">
#                   Cras justo odio
#                   <span class="badge bg-primary rounded-pill">14</span>
#                 </li>
#                 <li class="list-group-item d-flex justify-content-between align-items-center">
#                   Dapibus ac facilisis in
#                   <span class="badge bg-primary rounded-pill">2</span>
#                 </li>
#                 <li class="list-group-item d-flex justify-content-between align-items-center">
#                   Morbi leo risus
#                   <span class="badge bg-primary rounded-pill">1</span>
#                 </li>
#               </ul>
#             <button class="source-button btn btn-primary btn-xs" type="button" tabindex="0"><i class="bi bi-code"></i></button>
# </div>
page.locator("div.bs-component > ul.list-group")

# Pseudo Classes

# <h1 id="navbars">Navbars</h1>
page.locator("h1:text('Navbars')")
page.locator("h1:text('Nav')")

# Exact
page.locator("h1:text-is('Navs')")

# <div class="dropdown-menu show" aria-labelledby="btnGroupDrop1" style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(0px, 40px);" data-popper-placement="bottom-start">
#                     <a class="dropdown-item" href="#">Dropdown link</a>
#                     <a class="dropdown-item" href="#">Dropdown link</a>
# </div>
page.locator("div.dropdown-menu:visible")

# <button type="button" class="btn btn-primary">Primary</button>
page.locator(":nth-match(button.btn-primary, 5)")
page.locator(":nth-match(button:text('Primary'), 1)")



# -------------------------------- XPath -------------------------------- #


page.locator("//h1[contains(text(),'Head')]")
page.locator("//button[contains(@class, 'btn-outline-primary')]")
page.locator("//input[contains(@value, 'correct value')]")



# -------------------------------- Other -------------------------------- #


# nth locator
page.get_by_role("button", name="Primary").locator("nth=2")

# By Keyword
page.locator("id=btnGroupDrop1").highlight()

# By Visibility
page.locator("div.dropdown-menu").locator("visible=true").highlight()

# Getting Parent
page.get_by_label("Email address").locator("..").highlight()

# Filter
page.get_by_role("heading").filter(has_text="Heading").highlight()

# By Element inside of element
page.locator("div.form-label").filter(has=page.get_by_label("Password")).highlight()


# -------------------------------- Mouse Actions -------------------------------- #


button = page.locator("div.bs-component button[data-bs-toggle='popover']").filter(has=page.get_by_text("Left"))
button.click()
button.dblclick(delay=500)
button.click(button="right")
button.click(modifiers=["Shift", "Alt", "Control", "Meta"])
button.hover()


# -------------------------------- Input Field Actions -------------------------------- #


email_input = page.locator("input#exampleInputEmail1").highlight()

# Simulates CTRL + C and CTRL + V
email_input.fill("test@email.com")

# Simulates actually typing
email_input.type("test@email.com", delay=200)

# Gets current value inside input box (NOT placeholder value)
email_input.input_value()
email_input.clear()


# -------------------------------- Checkbox and Radio Inputs -------------------------------- #


radio1 = page.locator("input.form-check-input[value='option1']")
radio1.check()

checkbox1 = page.get_by_label("Default checkbox")
checkbox1.check()
checkbox1.uncheck()
checkbox1.is_checked()
checkbox1.set_checked(True)
checkbox1.click()


# -------------------------------- Option/Select Menu -------------------------------- #


select = page.get_by_label("Example select")
select.select_option("3")

multiple_select = page.get_by_label("Example multiple select").highlight()
multiple_select.select_option(["2", "4"])


# -------------------------------- Option/Select Menu -------------------------------- #


dropdown = page.locator("button#btnGroupDrop1")
dropdown.click()

dropdown2 = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last
dropdown2.click()


# -------------------------------- Uploading File -------------------------------- #


file_input = page.get_by_label("Default file input example")

with page.expect_file_chooser() as fc_info:
    file_input.click()

file_chooser = fc_info.value
file_chooser.set_files("app.py")

# ----------------------------------- Get Alt Text ----------------------------------- #


# Website: https://unsplash.com/

# <img loading="lazy" sizes="(min-width: 1335px) 410.6666666666667px, (min-width: 992px) calc(calc(100vw - 88px) / 3), 
# (min-width: 768px) calc(calc(100vw - 64px) / 2), 100vw" 
# srcset="https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=100&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 100w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=200&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 200w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=300&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 300w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=400&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 400w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=500&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 500w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=600&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 600w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=700&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 700w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=800&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 800w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=900&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 900w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=1000&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 1000w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=1200&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 1200w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=1400&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 1400w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=1600&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 1600w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=1800&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 1800w, 
# https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?w=2000&amp;auto=format&amp;fit=crop&amp;q=60&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8 2000w" 
# src="https://images.unsplash.com/photo-1720814989164-9dd27c24dcac?fm=jpg&amp;q=60&amp;w=3000&amp;ixlib=rb-4.0.3&amp;ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8" 
# alt="A lone sailboat in the middle of the ocean" itemprop="thumbnailUrl" class="ApbSI z1piP vkrMA" style="aspect-ratio:3851 / 5776" data-test="photo-grid-masonry-img">
page.get_by_alt_text("A lone sailboat in the middle of the ocean")

