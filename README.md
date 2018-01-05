# Welcome to CMU KGSA!

This repository holds a source code for the website for CMU KGSA.

***

### HOWTO: edit/improve the website

If you are a CMU KGSA admin who is willing to improve this website, please read this section.

Currently, there are four html pages that will be most frequently visited: *{index, about, life, career}.html*.

* **index.html** holds the front page.
* **about.html** introduces purpose, function, structure and organization of CMU KGSA.
* **life.html** shows two life wikis: settling in guide and living tips. It is a static page without any editing function. It would be good to implement such user-editing 
* **career.html** presents recent recruiting events (pulled from cmu.kgsa.career google calendar) and sponsorship

Currently our website is based on [Bootstrap](https://getbootstrap.com/), does not use any open source 'board' services such as xeboard. Main motivation behind this is to not use database, as it needs an active server to store and retrieve all website data. Instead, we decided to keep our website static, show minimal information necessary, and guide people to the adequate websites (i.e, CMU KGSA Facebook group, KDisTech Facebook group, CMU KGSA Bridge homepage, etc.) to meet their needs. If for some reason this has changed, please feel free to implement database-based services to the website.

If you are trying to do a minor edit to the website without altering current Bootstrap-based static style, referring to each html files will be enough to figure out which parts to edit. If you have to add a new CSS rule or Javascript code, [*creative.css*](css/creative.css) and [*creative.js*](js/creative.js) holds stylesheet rules and Javascript codes for all four pages. For *career.html*, [*calendar.js*](js/calendar.js) contains JQuery code to read calendar events and prints recent events. Minified _*.js_ and _*.css_ files are imported to each page, so when you are dealing with these files, make sure that you first change link of each file from minified to normal version to see any changes.

Please contact [here](mailto:fishhyuk11@gmail.com) if there is anything we can help.

*last modified by Gihyuk Ko, 12/06/2017*