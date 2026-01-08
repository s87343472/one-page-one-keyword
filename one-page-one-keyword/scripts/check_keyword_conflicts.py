#!/usr/bin/env python3
"""
关键词冲突检查脚本
检查关键词布局表中是否存在关键词重复/冲突的问题
"""

import csv
import sys
from collections import defaultdict
from typing import Dict, List, Set


def load_keyword_layout(csv_file: str) -> List[Dict]:
    """加载关键词布局CSV文件"""
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"错误: 找不到文件 {csv_file}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: 读取文件失败 - {e}")
        sys.exit(1)


def extract_keywords(row: Dict) -> Set[str]:
    """从一行中提取所有关键词"""
    keywords = set()
    
    # 主关键词
    if row.get('主关键词'):
        keywords.add(row['主关键词'].strip().lower())
    
    # 次要关键词
    for i in range(1, 6):
        key = f'次要关键词{i}'
        if row.get(key) and row[key].strip():
            keywords.add(row[key].strip().lower())
    
    return keywords


def check_conflicts(data: List[Dict]) -> Dict[str, List[str]]:
    """检查关键词冲突"""
    # 关键词 -> 页面URL列表
    keyword_to_pages = defaultdict(list)
    
    for row in data:
        url = row.get('页面URL', '未知URL')
        keywords = extract_keywords(row)
        
        for keyword in keywords:
            keyword_to_pages[keyword].append(url)
    
    # 找出有冲突的关键词
    conflicts = {}
    for keyword, pages in keyword_to_pages.items():
        if len(pages) > 1:
            conflicts[keyword] = pages
    
    return conflicts


def check_primary_keyword_issues(data: List[Dict]) -> List[Dict]:
    """检查主关键词相关问题"""
    issues = []
    
    for row in data:
        url = row.get('页面URL', '未知URL')
        primary = row.get('主关键词', '').strip()
        
        # 检查是否缺少主关键词
        if not primary:
            issues.append({
                'type': '缺少主关键词',
                'url': url,
                'message': '页面没有设置主关键词'
            })
        
        # 检查主关键词是否也作为次要关键词
        secondary_keywords = []
        for i in range(1, 6):
            key = f'次要关键词{i}'
            if row.get(key) and row[key].strip():
                secondary_keywords.append(row[key].strip().lower())
        
        if primary.lower() in secondary_keywords:
            issues.append({
                'type': '主次关键词重复',
                'url': url,
                'message': f'主关键词"{primary}"不应同时作为次要关键词'
            })
    
    return issues


def print_report(conflicts: Dict, issues: List[Dict]):
    """打印检查报告"""
    print("\n" + "="*80)
    print("关键词布局检查报告")
    print("="*80 + "\n")
    
    # 冲突报告
    if conflicts:
        print("⚠️  发现关键词冲突:")
        print("-" * 80)
        for keyword, pages in sorted(conflicts.items()):
            print(f"\n关键词: '{keyword}'")
            print(f"  冲突页面数量: {len(pages)}")
            print(f"  涉及页面:")
            for page in pages:
                print(f"    - {page}")
        print()
    else:
        print("✅ 未发现关键词冲突\n")
    
    # 其他问题报告
    if issues:
        print("⚠️  发现其他问题:")
        print("-" * 80)
        
        # 按类型分组
        issues_by_type = defaultdict(list)
        for issue in issues:
            issues_by_type[issue['type']].append(issue)
        
        for issue_type, issue_list in sorted(issues_by_type.items()):
            print(f"\n{issue_type} ({len(issue_list)}个):")
            for issue in issue_list:
                print(f"  - {issue['url']}: {issue['message']}")
        print()
    else:
        print("✅ 未发现其他问题\n")
    
    # 总结
    total_issues = len(conflicts) + len(issues)
    if total_issues == 0:
        print("🎉 恭喜!关键词布局完全符合'一个页面一个关键词'原则!")
    else:
        print(f"📊 总计发现 {total_issues} 个需要处理的问题")
    
    print("\n" + "="*80 + "\n")


def main():
    if len(sys.argv) < 2:
        print("用法: python check_keyword_conflicts.py <关键词布局表.csv>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    
    print(f"正在检查文件: {csv_file}")
    
    # 加载数据
    data = load_keyword_layout(csv_file)
    print(f"已加载 {len(data)} 个页面的关键词数据\n")
    
    # 检查冲突
    conflicts = check_conflicts(data)
    
    # 检查其他问题
    issues = check_primary_keyword_issues(data)
    
    # 打印报告
    print_report(conflicts, issues)
    
    # 返回错误代码
    if conflicts or issues:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
