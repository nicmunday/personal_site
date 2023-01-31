#!/usr/bin/env python3
from tkinter import *
from imports import newsprocessor
import webbrowser
import pathlib

window = Tk()
window.title("News")
window.geometry("1340x800")
window.configure(bg="black")


canvas = Canvas(window,
                width=1050,
                height=804,
                background="black",
                highlightthickness=0)

scroll_y = Scrollbar(window,
                     orient="vertical",
                     command=canvas.yview,
                     bg="#ff6600",
                     troughcolor="black",
                     highlightthickness=0,
                     highlightcolor="black",
                     highlightbackground="black",
                     bd=0)
scroll_y.grid(row=0, column=1,
              sticky="ns", rowspan=140)

def scrolldown(event):
    canvas.yview_scroll(
        -1*(event.delta-1), "units")
def scrollup(event):
    canvas.yview_scroll(
        -1*(event.delta+1), "units")

window.bind_all("<Button-4>", scrollup)
canvas.bind_all("<Button-5>", scrolldown)
window.bind_all("<Up>", scrollup)
canvas.bind_all("<Down>", scrolldown)

canvas.grid(row=1, column=0,rowspan=140, padx=(20,5))


links = IntVar(window, 1)
summaries = IntVar(window, 1)
story_pub = IntVar(window, 1)

links_button = Checkbutton(text="Include Links",
                      background="black",
                      foreground="#ff6600",
                      anchor=W,
                      highlightthickness=0,
                      width=25,
                      activebackground="#ff6600",
                      activeforeground="black",
                      cursor="arrow",
                      selectcolor="black",
                           variable=links)

summaries_button = Checkbutton(text="Include Summaries",
                      background="black",
                      foreground="#ff6600",
                      anchor=W,
                      highlightthickness=0,
                      width=25,
                      activebackground="#ff6600",
                      activeforeground="black",
                      cursor="arrow",
                      selectcolor="black",
                               variable=summaries)
story_pub_button = Checkbutton(text="Include Story Published Date",
                      background="black",
                      foreground="#ff6600",
                      anchor=W,
                      highlightthickness=0,
                      width=25,
                      activebackground="#ff6600",
                      activeforeground="black",
                      cursor="arrow",
                      selectcolor="black",
                               variable=story_pub)


stories_time_frame = StringVar(window, "1")

today = Radiobutton(text="Stories From Today",
                    background="black",
                     foreground="#ff6600",
                    anchor=W,
                    highlightthickness=0,
                    width=25,
                      activebackground="#ff6600",
                    activeforeground="black",
                    cursor="arrow",
                      selectcolor="black",
                    variable=stories_time_frame,
                    value="today")

not_today = Radiobutton(text=
                        "Stories From Before Today",
                        background="black",
                        foreground="#ff6600",
                        anchor=W,
                        highlightthickness=0,
                        width=25,
                        activebackground="#ff6600",
                        activeforeground="black",
                        cursor="arrow",
                      selectcolor="black",
                        variable=stories_time_frame,
                        value="not_today")

any_time = Radiobutton(text="Stories From Any Time",
                       background="black",
                       foreground="#ff6600",
                       anchor=W,
                       highlightthickness=0,
                       width=25,
                       activebackground="#ff6600",
                       activeforeground="black",
                       cursor="arrow",
                       selectcolor="black",
                       variable=stories_time_frame,
                       value="all",)

spacer = Label(width=1, background="black")

any_time.select()

only_new = IntVar(window, 0)
only_new_button = Checkbutton(text="Only New Stories",
                       background="black",
                      foreground="#ff6600",
                       anchor=W,
                       highlightthickness=0,
                       width=25,
                      activebackground="#ff6600",
                       activeforeground="black",
                       cursor="arrow",
                      selectcolor="black",
                       variable=only_new)

story_results = Label(text="",
                      background="black",
                      foreground="#ff6600",
                     anchor=W,
                     highlightthickness=0,
                      font=("Arial", 16))

current_time = Label(text="",
                      background="black",
                      foreground="#ff6600",
                     anchor=W,
                     highlightthickness=0,
                      font=("Arial", 16))

published_time = Label(text="",
                      background="black",
                      foreground="#ff6600",
                     anchor=W,
                     highlightthickness=0,
                      font=("Arial", 16))








def open_link(url):
   webbrowser.open_new_tab(url)


def get_news():

    my_news = newsprocessor.NewsProcessor()

    canvas.delete(ALL)
    canvas.config(height=804)
    stories = my_news.all_stories()
    stories.reverse()
    if stories_time_frame.get() == "today":
        stories = my_news.today_stories(stories)
    elif stories_time_frame.get() == "not_today":
        stories = my_news.not_today_stories(stories)

    if only_new.get() == 1:
        stories = my_news.new_stories(stories)

    i = 10
    x = 0
    canvas.create_text(0, 10, text="")
    for n in range(len(stories)):

        dynamic_var = f"label{x}"
        vars()[dynamic_var] = \
            canvas.create_text(0,
                               i,
                               text=f"{stories[n]['story']}",
                               font=("Arial", 15),
                               fill="#ff6600",
                               anchor=NW,
                               tags="textTag")
        i += 40
        x+=1
        if story_pub.get() == 1:
            dynamic_var = f"label{x}"
            vars()[dynamic_var] = \
                canvas.create_text(0,
                                   i-18,
                                   text=f"{stories[n]['gui_pub_string']}",
                                   font=("Arial", 12),
                                       fill="#009171",
                                   anchor=NW,
                                   tags="textTag",
                                   width=1030)
            i += 18
            x+=1
        if summaries.get() == 1:
            dynamic_var = f"label{x}"
            vars()[dynamic_var] = \
                canvas.create_text(0,
                                   i-20,
                                   text=f"{stories[n]['summary']}",
                                   font=("Arial", 12),
                                       fill="#e03663",
                                   anchor=NW,
                                   tags="textTag",
                                   width=1030)
            if len(stories[n]["summary"]) > 142:
                i+=20
            i += 18
            x+=1
        if links.get() == 1:
            dynamic_var = f"label{x}"
            vars()[dynamic_var] = \
                canvas.create_text(0,
                                   i-23,
                                   text=f"{stories[n]['link']}",
                                   font=("Arial", 12),
                                   fill="#0262c4",
                                   activefill= "#51f505" ,
                                   anchor=NW,
                                   tags="textTag")

            canvas.tag_bind(vars()[dynamic_var],
                            "<Button-1>",
                            lambda e, link=stories[n]['link']:
                            open_link(link))
            i += 16
            x+=1

    current_path = pathlib.Path(__file__).parent
    news_file = current_path.joinpath("imports",
                                          "text_files",
                                      "newsaccessed.txt")
    news_file.write_text((str(my_news.now)))

    story_results.config(
        text=f"{len(stories)} Stories Displayed")
    current_time.config(
        text=f"Display Time:\n"
             f"{my_news.now.strftime('%a %d %b %H:%M')}")
    published_time.config(
        text=f"Feed Published:\n"
             f"{my_news.rss_published_string}")

    canvas.create_text(0, i, text="")
    canvas.configure(yscrollcommand=scroll_y.set)
    canvas.configure(scrollregion=canvas.bbox(ALL))


get_stories = Button(text="Get Stories",
                     background="black",
                      foreground="#ff6600",
                     anchor=W,
                     highlightthickness=0,
                      activebackground="#ff6600",
                     activeforeground="black",
                     cursor="arrow",
                     justify=CENTER,
                     command=get_news)




spacer.grid(row=0, rowspan=49, column=3)
links_button.grid(row=6, column=4, columnspan=8)
summaries_button.grid(row=5, column=4, columnspan=8)
story_pub_button.grid(row=7, column=4, columnspan=8)
today.grid(row=18, column=4, columnspan=8)
not_today.grid(row=19, column=4, columnspan=8)
any_time.grid(row=20, column=4, columnspan=8)
only_new_button.grid(row=30, column=4, columnspan=8)
get_stories.grid(row=45, column=4,columnspan=8)
story_results.grid(row=60,column=3,columnspan=9, padx=(12,0))
current_time.grid(row=75,column=3,columnspan=9, padx=(12,0))
published_time.grid(row=90,column=3,columnspan=9, padx=(12,0))



window.mainloop()