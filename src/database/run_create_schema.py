import sqlite3
import sys
from pathlib import Path


def execute_sql_file(db_path: str, sql_file: str):

    sql_path = Path(sql_file)
    
    if not sql_path.exists():
        print(f"Arquivo SQL não encontrado: {sql_file}")
        sys.exit(1)
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        with open(sql_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        cursor.executescript(sql_script)
        conn.commit()
        
        print(f"Script executado com sucesso!")
        print(f"Banco de dados: {db_path}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Erro ao executar SQL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    
    current_dir = Path(__file__).parent
    db_path = current_dir / "songs.db"
    sql_file = current_dir / "create_schema.sql"
    
    execute_sql_file(str(db_path), str(sql_file))
