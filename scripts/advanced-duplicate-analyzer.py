#!/usr/bin/env python3
"""
Advanced Duplicate Detection System for 177-Agent Collection
Analyzes agents for duplicates, similarity, and creates optimization recommendations
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict
from difflib import SequenceMatcher
import yaml

class AgentDuplicateAnalyzer:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.agents = []
        self.duplicates = []
        self.similarity_threshold = 0.7
        self.slug_variations = defaultdict(list)

    def load_all_agents(self) -> List[Dict]:
        """Load all agent JSON files from directory structure"""
        agents = []

        for json_file in self.root_dir.rglob("*.json"):
            if json_file.name in ['ALL_AGENTS_COMBINED.json', 'MASTER_INDEX.json', '00-MASTER-INDEX.json']:
                continue

            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                if 'customModes' in data and isinstance(data['customModes'], list):
                    for agent in data['customModes']:
                        agent['_source_file'] = str(json_file)
                        agent['_category'] = json_file.parent.name
                        agents.append(agent)

            except Exception as e:
                print(f"⚠️  Error loading {json_file}: {e}")

        self.agents = agents
        print(f"✅ Loaded {len(agents)} agents from {len(list(self.root_dir.rglob('*.json')))} files")
        return agents

    def normalize_slug(self, slug: str) -> str:
        """Normalize slug for comparison (handle variations like full-stack vs fullstack)"""
        normalized = slug.lower()
        normalized = re.sub(r'[-_\s]+', '', normalized)  # Remove separators
        normalized = re.sub(r'(specialist|expert|engineer|developer|pro|master)', '', normalized)  # Remove common suffixes
        return normalized

    def calculate_similarity(self, agent1: Dict, agent2: Dict) -> float:
        """Calculate similarity score between two agents"""

        # Slug similarity (high weight)
        slug1_norm = self.normalize_slug(agent1.get('slug', ''))
        slug2_norm = self.normalize_slug(agent2.get('slug', ''))
        slug_similarity = SequenceMatcher(None, slug1_norm, slug2_norm).ratio()

        # Name similarity
        name1 = re.sub(r'[🎯🚀⚡🔧🎮📊🔍🤖💼🎯🏗️👨‍💻🛠️🔒📈💰]', '', agent1.get('name', '')).strip()
        name2 = re.sub(r'[🎯🚀⚡🔧🎮📊🔍🤖💼🎯🏗️👨‍💻🛠️🔒📈💰]', '', agent2.get('name', '')).strip()
        name_similarity = SequenceMatcher(None, name1.lower(), name2.lower()).ratio()

        # Role definition similarity
        role1 = agent1.get('roleDefinition', '')[:200]  # First 200 chars
        role2 = agent2.get('roleDefinition', '')[:200]
        role_similarity = SequenceMatcher(None, role1.lower(), role2.lower()).ratio()

        # Weighted average
        similarity = (slug_similarity * 0.5 + name_similarity * 0.3 + role_similarity * 0.2)

        return similarity

    def find_duplicates(self) -> List[Dict]:
        """Find duplicate agents using advanced similarity analysis"""
        duplicates = []
        processed = set()

        for i, agent1 in enumerate(self.agents):
            if i in processed:
                continue

            similar_agents = []

            for j, agent2 in enumerate(self.agents[i+1:], i+1):
                if j in processed:
                    continue

                similarity = self.calculate_similarity(agent1, agent2)

                if similarity >= self.similarity_threshold:
                    similar_agents.append({
                        'agent': agent2,
                        'similarity': similarity,
                        'index': j
                    })

            if similar_agents:
                # Group duplicates
                duplicate_group = {
                    'primary': agent1,
                    'primary_index': i,
                    'duplicates': similar_agents,
                    'group_size': len(similar_agents) + 1
                }
                duplicates.append(duplicate_group)

                # Mark as processed
                processed.add(i)
                for similar in similar_agents:
                    processed.add(similar['index'])

        self.duplicates = duplicates
        return duplicates

    def analyze_quality(self, agent: Dict) -> int:
        """Analyze agent quality based on completeness and detail"""
        score = 0

        # Basic fields
        if agent.get('slug'): score += 10
        if agent.get('name'): score += 10
        if agent.get('roleDefinition'): score += 20

        # Instructions quality
        instructions = agent.get('customInstructions', '')
        if len(instructions) > 1000: score += 20
        if len(instructions) > 5000: score += 20
        if len(instructions) > 10000: score += 30

        # Advanced features
        if 'MCP Tool' in instructions: score += 15
        if 'Communication Protocol' in instructions: score += 15
        if '```' in instructions: score += 10  # Code examples
        if 'optimization' in instructions.lower(): score += 10
        if 'security' in instructions.lower(): score += 10

        # Groups
        groups = agent.get('groups', [])
        score += len(groups) * 5

        return score

    def recommend_best_agent(self, duplicate_group: Dict) -> Dict:
        """Recommend which agent to keep from duplicate group"""
        all_agents = [duplicate_group['primary']] + [d['agent'] for d in duplicate_group['duplicates']]

        scored_agents = []
        for agent in all_agents:
            quality_score = self.analyze_quality(agent)
            scored_agents.append({
                'agent': agent,
                'quality_score': quality_score,
                'file': agent.get('_source_file', ''),
                'category': agent.get('_category', '')
            })

        # Sort by quality score
        scored_agents.sort(key=lambda x: x['quality_score'], reverse=True)

        return scored_agents[0]

    def create_category_taxonomy(self) -> Dict:
        """Create optimized category taxonomy"""

        # Analyze existing categories
        category_counts = defaultdict(int)
        for agent in self.agents:
            category_counts[agent.get('_category', 'unknown')] += 1

        # Proposed new taxonomy based on analysis
        new_taxonomy = {
            "core-development": {
                "description": "Essential development roles",
                "subcategories": ["architecture", "fullstack", "backend", "frontend"]
            },
            "language-specialists": {
                "description": "Programming language experts",
                "subcategories": ["python", "javascript", "typescript", "golang", "rust", "java", "csharp"]
            },
            "infrastructure-devops": {
                "description": "Infrastructure and operations",
                "subcategories": ["cloud", "kubernetes", "docker", "networking", "monitoring"]
            },
            "ai-ml": {
                "description": "AI and machine learning",
                "subcategories": ["llm", "computer-vision", "nlp", "data-science", "mlops"]
            },
            "business-product": {
                "description": "Business and product management",
                "subcategories": ["product-management", "business-analysis", "marketing", "sales"]
            },
            "security-quality": {
                "description": "Security and quality assurance",
                "subcategories": ["security-audit", "testing", "compliance", "accessibility"]
            },
            "specialized-domains": {
                "description": "Domain-specific experts",
                "subcategories": ["fintech", "gaming", "iot", "blockchain", "legal"]
            },
            "meta-orchestration": {
                "description": "Agent coordination and workflow",
                "subcategories": ["orchestration", "coordination", "workflow", "monitoring"]
            }
        }

        return new_taxonomy

    def generate_report(self) -> str:
        """Generate comprehensive analysis report"""
        report = []
        report.append("# 🔍 ADVANCED DUPLICATE ANALYSIS REPORT")
        report.append(f"**Total Agents Analyzed**: {len(self.agents)}")
        report.append(f"**Duplicate Groups Found**: {len(self.duplicates)}")

        # Category distribution
        report.append("\n## 📊 Current Category Distribution")
        category_counts = defaultdict(int)
        for agent in self.agents:
            category_counts[agent.get('_category', 'unknown')] += 1

        for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
            report.append(f"- **{category}**: {count} agents")

        # Duplicate analysis
        if self.duplicates:
            report.append("\n## 🔄 Duplicate Groups Analysis")

            total_duplicates = sum(d['group_size'] for d in self.duplicates)
            unique_agents = len(self.agents) - total_duplicates + len(self.duplicates)

            report.append(f"**Potential Space Savings**: {total_duplicates - len(self.duplicates)} agents")
            report.append(f"**Optimized Collection Size**: {unique_agents} agents")

            for i, dup_group in enumerate(self.duplicates[:10], 1):  # Show top 10
                primary = dup_group['primary']
                report.append(f"\n### Group {i}: {primary.get('slug', 'unknown')}")
                report.append(f"**Primary**: {primary.get('name', 'Unknown')} ({primary.get('_category', 'unknown')})")

                for dup in dup_group['duplicates']:
                    agent = dup['agent']
                    similarity = dup['similarity']
                    report.append(f"- **Similar**: {agent.get('name', 'Unknown')} ({agent.get('_category', 'unknown')}) - {similarity:.1%} match")

                # Recommendation
                best = self.recommend_best_agent(dup_group)
                report.append(f"**Recommended**: Keep {best['agent'].get('slug')} (Quality Score: {best['quality_score']})")

        # Quality analysis
        report.append("\n## 🏆 Quality Distribution")
        quality_scores = [self.analyze_quality(agent) for agent in self.agents]
        avg_quality = sum(quality_scores) / len(quality_scores)
        high_quality = len([s for s in quality_scores if s > avg_quality * 1.2])

        report.append(f"**Average Quality Score**: {avg_quality:.1f}")
        report.append(f"**High Quality Agents**: {high_quality} ({high_quality/len(self.agents):.1%})")

        # Proposed taxonomy
        taxonomy = self.create_category_taxonomy()
        report.append("\n## 🗂️ Proposed Optimized Taxonomy")
        for category, info in taxonomy.items():
            report.append(f"### {category}")
            report.append(f"*{info['description']}*")
            subcats = ", ".join(info['subcategories'])
            report.append(f"**Subcategories**: {subcats}")

        return "\n".join(report)

    def export_duplicate_matrix(self) -> Dict:
        """Export detailed duplicate analysis for processing"""
        return {
            'total_agents': len(self.agents),
            'duplicate_groups': len(self.duplicates),
            'duplicates': [
                {
                    'primary_slug': group['primary'].get('slug'),
                    'primary_file': group['primary'].get('_source_file'),
                    'primary_quality': self.analyze_quality(group['primary']),
                    'similar_agents': [
                        {
                            'slug': dup['agent'].get('slug'),
                            'file': dup['agent'].get('_source_file'),
                            'similarity': dup['similarity'],
                            'quality': self.analyze_quality(dup['agent'])
                        }
                        for dup in group['duplicates']
                    ],
                    'recommended': self.recommend_best_agent(group)['agent'].get('slug')
                }
                for group in self.duplicates
            ],
            'category_counts': dict(defaultdict(int, {
                agent.get('_category', 'unknown'): 1
                for agent in self.agents
            })),
            'proposed_taxonomy': self.create_category_taxonomy()
        }

def main():
    analyzer = AgentDuplicateAnalyzer('/tmp/roo-modes')

    print("🔍 Loading all agents...")
    agents = analyzer.load_all_agents()

    print("🔄 Analyzing for duplicates...")
    duplicates = analyzer.find_duplicates()

    print("📊 Generating analysis report...")
    report = analyzer.generate_report()

    # Save report
    with open('/tmp/roo-modes/DUPLICATE_ANALYSIS_REPORT.md', 'w') as f:
        f.write(report)

    # Save detailed analysis
    analysis_data = analyzer.export_duplicate_matrix()
    with open('/tmp/roo-modes/duplicate-analysis.json', 'w') as f:
        json.dump(analysis_data, f, indent=2)

    print("✅ Analysis complete!")
    print(f"📄 Report saved to: DUPLICATE_ANALYSIS_REPORT.md")
    print(f"📊 Data saved to: duplicate-analysis.json")

    # Quick summary
    total_duplicates = sum(d['group_size'] for d in duplicates)
    if duplicates:
        print(f"\n🎯 SUMMARY:")
        print(f"   Found {len(duplicates)} duplicate groups")
        print(f"   Potential reduction: {total_duplicates - len(duplicates)} agents")
        print(f"   Optimized size: {len(agents) - (total_duplicates - len(duplicates))} agents")
    else:
        print(f"\n✨ No duplicates found in {len(agents)} agents!")

if __name__ == "__main__":
    main()