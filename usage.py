from bo_freq_diff import *
from pathlib import Path
import time

orig = 'བཀྲ་ ཤིས་ བདེ་ ལེགས།'
new = 'བཀྲ་ ཤས་ བདེ་ ལེག།'

dmp = DMP()
diffs = dmp.diff_wordMode(orig, new)
print(diffs)
# [(0, 'བཀྲ་ '), (-1, 'ཤིས་ '), (1, 'ཤས་ '), (0, 'བདེ་ '), (-1, 'ལེགས།'), (1, 'ལེག།')]


sd = SyllableDiff()
orig = '༄༅༅། །རྒྱ་གར་སྐད་དུ། ཨརྱ་མ་ཧ་པ་རི་ནི་རྦ་ཎ་ན་མ་མ་ཧ་ཡ་ན་སུ་ཏྲ། བོད་སྐད་དུ། འཕགས་པ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ཐེག་པ་ཆེན་པོའི་མདོ། །། བམ་པོ་དང་པོ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །འདི་སྐད་བདག་གིས་ཐོས་པ་དུས་གཅིག་ན།'
orig = orig.replace(' ', '_')
new = """༄༅། །མདོ་སྡེ་ཐ་པ་བཞུགས་སོ།། 
[1b]
[1b.1]{T120}༄༅༅། །རྒྱ་གར་སྐད་དུ། ཨཱརྱ་མ་ཧཱ་པ་རི་ནིརྦཱ་ཎ་ནཱ་མ་མ་ཧཱ་ཡཱ་ན་སཱུ་ཏྲ། བོད་སྐད་དུ། འཕགས་པ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ཐེག་པ་ཆེན་པོའི་མདོ། བམ་པོ་
[1b.2]དང་པོ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །འདི་སྐད་བདག་གིས་ཐོས་པ་དུས་གཅིག་ན།""".replace('\n', '–').replace(' ', '_')
diffs = sd.diff(orig, new)
print(diffs)
# ['བཀྲ་ ', {'-': 'ཤས་ ', '+': 'ཤིས་ '}, 'བདེ་ ', {'-': 'ལེག ', '+': 'ལེགས '}, '།']


od = OrderedDiff(orig, new)
joined_out = od.export_diffs(split_context=False)
print(joined_out)
# [
#     ['Freq/Type', 'L', 'A', 'B', 'R'],
#     ('1: -ཤས་+ཤིས་', '', '', '', ''),
#     ('', 'བཀྲ་', 'ཤས་', 'ཤིས་', 'བདེ་ལེགས།'),
#     ('1: -ལེག+ལེགས', '', '', '', ''),
#     ('', 'བཀྲ་ཤིས་བདེ་', 'ལེག', 'ལེགས', '།'),
# ]


split_out = od.export_diffs()
print(split_out)
# [
#     ['Freq/Type', 'L5', 'L4', 'L3', 'L2', 'L1', 'A', 'B', 'R1', 'R2', 'R3', 'R4', 'R5'],
#     ['1: -ཤས་+ཤིས་', '', '', '', '', '', '', '', '', '', '', '', ''],
#     ['', '', '', '', '', 'བཀྲ་', 'ཤས་', 'ཤིས་', 'བདེ་', 'ལེགས', '།', '', ''],
#     ['1: -ལེག+ལེགས', '', '', '', '', '', '', '', '', '', '', '', ''],
#     ['', '', '', 'བཀྲ་', 'ཤིས་', 'བདེ་', 'ལེག', 'ལེགས', '།', '', '', '', ''],
# ]

od.write_to_csv(split_out, Path('test.csv'))


start = time.time()
diff_one_file(Path('53.txt'), Path('053-tagged.txt'), outfile=Path('53-diff.csv'))
end = time.time()
print(end-start)
