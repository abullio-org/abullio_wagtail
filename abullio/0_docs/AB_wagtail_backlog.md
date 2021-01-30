# AB_wagtail_backlog

Backlog and development notes

## local development

development of the abullio blog app on wagtail in the laptop environment

### Environment setup

- [x] create directory /home/paolo/Projects/abullio_wagtail
- [x] install pyenv <https://github.com/pyenv/pyenv#installation>
- [x] set pyenv local 3.8.3
- [x] install pyenv virtualenv <https://github.com/pyenv/pyenv-virtualenv> 

### django wagtail environment

- [x] create virtual env  wagtail

  ```bash
  $ pyenv virtualenv wagtail
  $ pyenv local wagtail
  ```

- [x] install wagtail <https://docs.wagtail.io/en/stable/getting_started/index.html>

- [x] start abullio project

  superuser username adminAbullio password IW7Qd9Brbmu7

  superuser email paolo.demagistris@abullio.org

  

### wagtail development - basic

follow <https://docs.wagtail.io/en/stable/getting_started/tutorial.html>

- [x] Extend home page
- [x] A basic blog
    * blog pages
    * parent and children queryset
    * overriding context
    * images
    * tags
    * categories
    
### Styling and theming
- [x] Styles
    * Understand SASS and CSS <https://youtu.be/Zz6eOVaaelI>
    * theming bootstrap <https://youtu.be/6Ovw43Dkp44>
    * go to ~/Projects/abullio_static using VScode
    * Choose base kit Bootstrap <https://getbootstrap.com/>
        * install via npm
    
- [x] LAyout for base.html and following templates
    * copied layout.html from static version in abullio/abullio/templates
    * fix styles references
    * test changing fonts
    * 
- [x] style parallax in scss
    * copied layout.html from static version in abullio/abullio/templates
    * see https://www.w3schools.com/howto/howto_css_parallax.asp
    * see https://jossingram.wordpress.com/2015/08/03/parallax-background-image-block-for-wagtails-streamfield/

- [ ] Add glyphicons
    * Install Fotn awesome 5 see https://www.w3schools.com/icons/fontawesome5_intro.asp

- [ ] Add unsplash wagtail app
    * Install https://github.com/jafacakes2011/wagtail-unsplash
    * Obtain unsplash keys
      * Access key fwtJ2vbpTzhfqP2YlbzMNv2pk2e3Cw321F8Hub4c7lg
      * Secret key d9Alo4gmzn4eeEZ2tuk9ne8f7eK95xIKzuRbEmwyPQI

### ...

### docker deployment

see [this video](https://youtu.be/nh1ynJGJuT8)


