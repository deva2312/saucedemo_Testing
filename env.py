import os



def after_all(context):
    context.driver.quit()
    report_dir = os.path.join(os.getcwd(), 'reports')
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    json_report_path = os.path.join(report_dir, 'report.json')
    with open(os.path.join(report_dir, 'custom_summary.txt'), 'w') as summary_file:
        summary_file.write(f'Total Scenarios: {context._runner.steps_passed + context._runner.steps_failed}\n')
        summary_file.write(f'Passed: {context._runner.steps_passed}\n')
        summary_file.write(f'Failed: {context._runner.steps_failed}\n')
    print(f"Reports generated in {report_dir}")
