class logo:
  @classmethod
  def tool_header(self):
    print('''

         
|Установка Хакерских программ |
         ''')


  @classmethod
  def tool_footer(self):
    print('''        
        ''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
❇️  Xack-Menu успешно установлен.
❇️  Запустить Xack-Menu.
❇️  Введите cicada в вашем терминале.''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
❇️ Используйте его на свой страх и риск.
❇️ Нет гарантии.
❇️ Используйте это только в законных целях.
❇️ Я не несу ответственности за ваши действия.
❇️ Не делайте то, что запрещено.

Если вы устанавливаете этот инструмент.
это означает, что вы согласны со всеми условиями.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
❇️ Xack-Menu  успешно установлен.
❇️ Запустить Xack-Menu .
❇️ Введите cicada в вашем терминале.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
0️⃣1️⃣  Обновите ваш Xack-Menu
0️⃣0️⃣  Вернуться.''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
❇️ Xack-Menu  успешно обновлен.
❇️ Нажмите Enter, чтобы продолжить.''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
❇️  Нет сетевого подключения?
❇️  Вы в автономном режиме?
❇️  Пожалуйста, попробуйте еще раз через некоторое время.''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
❇️  Установленна последняя версия Xack-Menu .
❇️  Пожалуйста, попробуйте еще раз через некоторое время.''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
❇️ Название :- Xack-Menu
❇️ Разроботчик :- Bednakov Denis
❇️ GitHub :- http://github.com/bednakovdenis
❇️ facebook :- https://www.facebook.com/cicada3301denis/
❇️ Обновление :- 19/01/2021.
❇️ инструменты :- всего {total} инструментов.

❇️ Это автоматический установщик программ.
❇️ Сделано для системы на основе termux и linux.
❇️ Используйте этот инструмент на свой страх и риск.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print ("""       
\|Выберите свой инструмент|
       """)

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
❇️ Извените ??
❇️ '{name}'\ уже установлено !!
        ''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
❇️ Успешно установлено!!
❇️ '{name}'\ успешно установлен!!
        ''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
❇️ Извини ??
❇️ '{name}' не установлено !!
        ''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""        
|0️⃣0️⃣  Назад                                  |
        """)

  @classmethod
  def updating(self):
    print (""" 
\|обновление|
 """)

  @classmethod
  def installing(self):
    print (""" 
\|Установка|
 """)

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
0️⃣1️⃣  Все[ Всего {total} ]
0️⃣2️⃣  Категории
0️⃣3️⃣  Обновление
0️⃣4️⃣  Про Меня
 ✖️  Выход.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
❇️ Спасибо за использование Xack-Menu
❇️ Пока.....:)''')
    self.tool_footer()
