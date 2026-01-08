#!/usr/bin/env python3
"""
Simple packaging script for one-page-one-keyword skill.
Creates a .skill file (which is a .zip file) from the skill folder.
"""

import os
import zipfile
from pathlib import Path

def package_skill(skill_folder: str, output_dir: str = "."):
    """Package the skill folder into a .skill file."""
    
    skill_path = Path(skill_folder)
    if not skill_path.exists():
        print(f"❌ Error: Skill folder '{skill_folder}' not found")
        return False
    
    # Check for required SKILL.md
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: SKILL.md not found in '{skill_folder}'")
        return False
    
    # Create output filename
    skill_name = skill_path.name
    output_path = Path(output_dir) / f"{skill_name}.skill"
    
    print(f"📦 Packaging skill: {skill_folder}")
    print()
    
    # Create zip file with .skill extension
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in skill_path.rglob('*'):
            if file_path.is_file():
                # Get relative path
                arc_name = file_path.relative_to(skill_path.parent)
                zipf.write(file_path, arc_name)
                print(f"  Added: {arc_name}")
    
    print()
    print(f"✅ Successfully packaged skill to: {output_path}")
    return True

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 package_skill.py <skill-folder> [output-dir]")
        print()
        print("Example:")
        print("  python3 package_skill.py one-page-one-keyword")
        print("  python3 package_skill.py one-page-one-keyword ./dist")
        sys.exit(1)
    
    skill_folder = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    
    success = package_skill(skill_folder, output_dir)
    sys.exit(0 if success else 1)
