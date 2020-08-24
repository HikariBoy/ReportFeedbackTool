# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'wkhtmltopdf.exe', '.' ),
         ( 'Medusa_img.png', '.' ),
         ( 'medusa.ico','.'),
         ( 'longhelp_icon.png','.')
         ]

a = Analysis(['grading_gui.py'],
             pathex=['.'],
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
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='GradingTool',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          uac_admin=False,
          console=False)
