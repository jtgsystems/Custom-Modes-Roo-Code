# Custom AI Agent Rules for Roo Code

This file defines unified natural language guidelines for AI agents following the 2025 Agent Rules Standard.

## Core Principles (2025 Standards)

### Security-First Development
- Never hardcode API keys, secrets, or credentials
- Implement input validation and sanitization for all user inputs
- Follow OWASP Top 10 security guidelines
- Use secure authentication and authorization patterns
- Validate all external data sources and API responses

### Performance Excellence
- Target sub-200ms API response times
- Implement efficient database queries with proper indexing
- Use caching strategies (memory, Redis, CDN) appropriately
- Optimize for scalability with 10x growth planning
- Monitor resource usage and implement auto-scaling

### Code Quality Standards
- Follow SOLID principles in all implementations
- Maintain files under 500 lines with single responsibility
- Achieve >90% test coverage with meaningful tests
- Use descriptive naming conventions and clean code practices
- Implement comprehensive error handling and logging

### Architecture Guidelines
- Design modular, extensible systems with clear boundaries
- Use dependency injection and interface segregation
- Implement hexagonal architecture patterns where appropriate
- Follow domain-driven design principles
- Ensure loose coupling and high cohesion

## Agent Behavior Guidelines

### Development Workflow
1. **Specification**: Always clarify requirements and constraints first
2. **Architecture**: Design modular, secure, and scalable solutions
3. **Implementation**: Write clean, tested, and documented code
4. **Validation**: Test thoroughly and verify security compliance
5. **Documentation**: Update all relevant documentation

### Communication Standards
- Provide clear, actionable responses
- Include code examples and explanations
- Suggest best practices and alternatives
- Flag potential security or performance issues
- Document decisions and trade-offs

### Tool Usage Patterns
- Use precise, atomic operations when possible
- Validate all parameters before execution
- Implement proper error handling and recovery
- Follow the principle of least privilege
- Log all significant operations for auditing

## 2025 Technology Standards

### Modern Development Stack
- TypeScript for type safety and better developer experience
- React 18+ with concurrent features and Suspense
- Node.js 20+ with native ESM support
- Docker for containerization and development consistency
- Kubernetes for orchestration and scaling

### AI/ML Integration
- Use structured prompts with clear context and constraints
- Implement multi-model validation for critical decisions
- Follow responsible AI practices with human oversight
- Optimize for cost and performance with model routing
- Maintain transparency in AI decision-making processes

### Testing & Quality Assurance
- Test-driven development (TDD) with red-green-refactor cycles
- Integration testing for API endpoints and data flows
- Security testing for common vulnerabilities
- Performance testing under load conditions
- Accessibility testing for inclusive design

## Project-Specific Guidelines

### File Organization
- Use consistent directory structure with clear separation of concerns
- Implement proper module boundaries and import patterns
- Maintain clean project root with essential files only
- Use meaningful file and directory naming conventions

### Code Review Standards
- Focus on security implications and business logic
- Validate architectural decisions and design patterns
- Ensure compliance with coding standards and conventions
- Check for proper error handling and edge cases
- Verify test coverage and quality

### Deployment & Operations
- Use infrastructure as code (IaC) for reproducible deployments
- Implement comprehensive monitoring and alerting
- Follow blue-green or canary deployment strategies
- Maintain rollback procedures and disaster recovery plans
- Use automated testing in CI/CD pipelines

## Compliance & Legal Considerations

### Data Protection
- Implement GDPR and privacy-by-design principles
- Use data minimization and purpose limitation
- Ensure proper data encryption and access controls
- Maintain audit trails for data processing activities

### Intellectual Property
- Respect open source licenses and attribution requirements
- Avoid copying proprietary code or algorithms
- Document all third-party dependencies and licenses
- Implement proper code review for IP compliance

---

*This AGENTS.md file follows the 2025 Agent Rules Standard for unified AI agent guidance across development tools.*