rem 親ディレクトリに　grammars-v4をダウンロードしておく
rem git clone https://github.com/antlr/grammars-v4.git
java -jar antlr-4.8-complete.jar -Dlanguage=Python3 -no-listener grammars-v4\cobol85\Cobol85.g4

java -jar antlr-4.8-complete.jar -Dlanguage=Python3 -no-listener grammars-v4\cobol85\Cobol85Preprocessor.g4
