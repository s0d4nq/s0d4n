import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send ('pong')

# HTML теги

@bot.command()
async def html(ctx):
    await ctx.send ('<h1>-<h6> =  Заголовки\n<b> = Жирное начертание шрифта\n<br> = Перенос текста на следующую сторку\n<a>= Ссылка\n<div> = Блочный элемент, управляется с помощью стилей\n<hr> = Рисует горизонтальную линию на всю ширину body\n <header> = Задает «шапку» сайта или раздела, в которой обычно располагается заголовок\n <img> = Предназначен для отображения изображения на сайте\n <li> = Определяет элемент списка для тегов <ol> и <ul>\n <link> = Устанавливает связь с внешним файлом CSS\n <main> = Предназначен для основного содержимого документа\n <aside> = Определяет блок сбоку от main для дополнительной информации\n <article> = Задает содержание сайта вроде новости\n <ol> = Устанавливает нумерованный список\n <p> = Определяет текстовый абзац\n <strong> = Предназначен для акцентирования текста\n <table> = Служит контейнером для элементов, определяющих содержимое таблицы\n <th> = Предназначен для создания одной ячейки таблицы, которая обозначается как заголовочная\n <tr> = Служит контейнером для создания строки таблицы\n <td> = Предназначен для создания одной ячейки таблицы в теге <tr>\n <title> = Определяет заголовок документа. Должен быть написан только в теге <head>\n <ul> = Устанавливает маркированный список \n <picture> =')

@bot.command()
async def picture(ctx):
    await ctx.send ('<picture></picture>')

@bot.command()
async def h1(ctx):
    await ctx.send ('Заголовок первого уровня (самый большой)\n <h1>text</h1>')

@bot.command()
async def h2(ctx):
    await ctx.send ('Заголовок второго уровня\n <h2>text</h2>')

@bot.command()
async def h3(ctx):
    await ctx.send ('Заголовок третьего уровня\n <h3>text</h3>')

@bot.command()
async def h4(ctx):
    await ctx.send ('Заголовок четвертого уровня\n <h4>text</h4>')

@bot.command()
async def h5(ctx):
    await ctx.send ('Заголовок пятого уровня\n <h5>text</h5>')     

@bot.command()
async def h6(ctx):
    await ctx.send ('Заголовок шестого уровня (самый маленький)\n <h6>text</h6>')

@bot.command()
async def b(ctx):
    await ctx.send ('<b>text</b>')

@bot.command()
async def br(ctx):
    await ctx.send ('text <br> text')

@bot.command()
async def a(ctx):
    await ctx.send ('<a href="путь к файлу или ссылка"> \n должен иметь атрибут href')

@bot.command()
async def div(ctx):
    await ctx.send ('<div>(теги)</div> \n изменяется при помощи CSS кода \n имеет максимальную ширину но имеет нулевую высоту')

@bot.command()
async def header(ctx):
    await ctx.send ('<header>(заголовок)</header>')

@bot.command()
async def img(ctx):
    await ctx.send ('<img href="(путь к файлу)" alt="(на сайте будет отображаться текст, если путь к файлу указан неправильно)" \n должен иметь атрибут href')

@bot.command()
async def li(ctx):
    await ctx.send ('<li>text</li>')

@bot.command()
async def link(ctx):
    await ctx.send ('<link href="путь к файлу" rel="stylesheet">')

@bot.command()
async def main(ctx):
    await ctx.send ('<main>теги</main>')

@bot.command()
async def aside(ctx):
    await ctx.send ('<aside>теги</aside>')

@bot.command()
async def article(ctx):
    await ctx.send ('<article>теги</article>')

@bot.command()
async def ol(ctx):
    await ctx.send ('<ol> \n    <li></li> \n </ol>')

@bot.command()
async def p(ctx):
    await ctx.send ('<p>text</p>')

@bot.command()
async def strong(ctx):
    await ctx.send ('<strong>text</strong>')

@bot.command()
async def table(ctx):
    await ctx.send ('<table>теги</table>')

@bot.command()
async def th(ctx):
    await ctx.send ('<tr> \n     <th>text</th> \n </tr>')

@bot.command()
async def tr(ctx):
    await ctx.send ('<table> \n <tr>теги</tr> \n </table>')

@bot.command()
async def td(ctx):
    await ctx.send ('<tr> \n    <td></td> \n </tr>')

@bot.command()
async def title(ctx):
    await ctx.send ('<title>Название страницы</title>')

@bot.command()
async def ul(ctx):
    await ctx.send ('<ul> \n    <li></li> \n </ul>')

#CSS свойства

@bot.command()
async def css(ctx):
    await ctx.send ('align-content = устанавливает распределение пространства между и вокруг элементов \n align-self = align-content только для одного отдельного элемента \n background = фон объекта \n border = граница объекта \n border-bottom = нижняя граница объекта \n border-left = левая граница объекта \n border-right = правая граница объекта \n border-top = верхняя граница объекта \n border-radius = закругление границы \n box-shadow = тень объекта \n color = цвет текста \n display = определяет, как должен отображаться html объект \n flex-flow = совмещение flex-direction и flex-wrap в одном теге \n flex-direction = направление объектов(flex) \n flex-wrap = задаёт правила вывода flex-элементов — в одну строку или в несколько, с переносом блоков \n float = размещение объекта слева и справо \n font-style = стиль шрифта \n font-weight = определяет толщину шрифта \n font-size = размер шрифта \n font-family = задает шрифт \n justify-content = задает выравнивание между элементами (flexbox) \n list-style-type = тип элемента списка \nmargin = внешний отступ \n margin-bottom = нижний внешний отступ \n margin-left = левый внешний отступ \n margin-right = правый внешний отступ \n margin-top = верхний внешний отступ \n opacity = прозрачность объекта \n order = устанавливает порядок элементов(flexbox) \n padding	= внутренний отступ \n padding-bottom = нижний внутренний отступ \n padding-left = левый внутренний отступ \n padding-right = правый внутренний отступ \n padding-top = верхний внутренний отступ \n text-align = выравнивание текста \n text-decoration = декорация текста \n transition = анимация объекта \n width = ширина объекта \n height = высота объекта \n border-collapse = граница таблиц \n')

@bot.command()
async def align_content(ctx):
    await ctx.send ('align-content - stretch(значение по умолчанию), center(выравнивает по центру ), flex-start(), flex-end(), space-between(), space-around(), space-evenly()')

bot.run('ODk3Mzk1MzMzNTkwNTY4OTYw.YWVCiA.fxApOXjNy4nIAZDtrLwFrP1JFO8')