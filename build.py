from pathlib import Path
import html,re
root=Path(__file__).parent
def inline(s):
 s=html.escape(s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:f'<a href="{m[2].replace("privacy-policy.md","privacy-policy.html")}">{m[1]}</a>',s)
def render(s):
 result=[]; listing=False; paragraph=[]
 def flush():
  if paragraph:result.append("<p>"+inline(" ".join(paragraph))+"</p>");paragraph.clear()
 for line in s.splitlines():
  if line.startswith('- '):
   flush()
   if not listing:result.append('<ul>');listing=True
   result.append('<li>'+inline(line[2:])+'</li>');continue
  if listing:result.append('</ul>');listing=False
  if not line.strip():flush();continue
  m=re.match(r'^(#{1,3}) (.*)',line)
  if m:flush();result.append(f'<h{len(m[1])}>{inline(m[2])}</h{len(m[1])}>')
  else:paragraph.append(line)
 if listing:result.append('</ul>')
 flush()
 return '\n'.join(result)
css='''*{box-sizing:border-box}html{color-scheme:light dark}body{margin:0;background:#f5f5f1;color:#222a28;font:17px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}header,main,footer{max-width:1020px;margin:auto;padding:24px 32px}header{display:flex;align-items:center;justify-content:space-between;gap:20px;border-bottom:1px solid #d8ddd7}nav{display:flex;gap:22px;flex-wrap:wrap;font-size:14px}a{color:#27644e;text-underline-offset:4px}nav a,.brand{text-decoration:none}.brand{font-weight:750;letter-spacing:-.5px;color:inherit}main{max-width:820px;padding-top:64px;padding-bottom:72px;overflow-wrap:anywhere}h1{font-size:clamp(36px,7vw,64px);line-height:1.12;letter-spacing:-2px;margin:0 0 28px}h2{font-size:25px;letter-spacing:-.6px;margin:44px 0 12px}h3{font-size:20px;margin:30px 0 10px}p{margin:0 0 20px}ul{padding-left:22px}li{margin:10px 0}footer{font-size:13px;color:#59645d;border-top:1px solid #d8ddd7}code{font-size:.88em}a:focus-visible{outline:3px solid #448f71;outline-offset:5px} .eyebrow{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#59645d;margin-bottom:22px}@media(prefers-color-scheme:dark){body{background:#111715;color:#e3eae5}a{color:#9cd7bb}header,footer{border-color:#324239}footer,.eyebrow{color:#a1b1a6}}@media(max-width:600px){header{align-items:flex-start;flex-direction:column}header,main,footer{padding-left:22px;padding-right:22px}main{padding-top:42px}nav{gap:12px 18px}h1{letter-spacing:-1px}}'''
(root/'style.css').write_text(css)
for path in (root/'content').glob('*.md'):
 zh=path.stem.endswith('-zh');title=path.read_text().splitlines()[0].lstrip('# ')
 nav='<a href="index.html">Home</a><a href="support.html">Support</a><a href="privacy-policy.html">Privacy</a><a href="legal.html">Licenses</a><a href="downloads.html">Downloads</a><a href="support-zh.html" lang="zh-Hans">中文</a>'
 switch=''
 if path.stem in ['support','privacy-policy','support-zh','privacy-policy-zh']:
  switch=f'<p><a href="{path.stem.removesuffix("-zh")+("" if zh else "-zh")}.html">'+('English' if zh else '简体中文')+'</a></p>'
 (root/(path.stem+'.html')).write_text(f'''<!doctype html>
<html lang="{'zh-Hans' if zh else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self'; base-uri 'none'; form-action 'none'"><title>{html.escape(title)} · Moonight Studio</title><meta name="description" content="RemoteFS support, privacy and third-party materials for Mac, iPhone and iPad."><link rel="stylesheet" href="style.css"></head><body><header><a class="brand" href="index.html">Moonight Studio / RemoteFS</a><nav aria-label="Main navigation">{nav}</nav></header><main><p class="eyebrow">RemoteFS · Support & resources</p>{switch}{render(path.read_text())}</main><footer>Moonight Studio · RemoteFS<br><a href="https://github.com/Moonight-Studio/RemoteFS/issues">Contact support</a> · <a href="https://github.com/Moonight-Studio/RemoteFS">Public materials</a></footer></body></html>''')
print('Built',len(list((root/'content').glob('*.md'))),'pages')
