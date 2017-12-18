# -*- mode: python -*-

block_cipher = None

a = Analysis(['game.py', 'TheShadowKingdom.spec'],
             pathex=['C:\\Users\\Aaron\\Dropbox\\GitHub\\TheShadowKingdom'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          Tree('Entities', prefix='Entities'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='The Shadow Kingdom',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='sword.ico')
