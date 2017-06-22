import click
import workflow
import logging
import numbers
import config


@click.command()
@click.argument('workflow_file')
def main(workflow_file):
    try:
        wf = workflow.Workflow(workflow_file)
        data = wf.run()
        res = '{}:\n'.format(workflow_file)
        for key, value in data.iteritems():
            if isinstance(value, str) or isinstance(value, numbers.Number):
                print '{}: {}'.format(key, value)
                res += '{}: {}\n'.format(key, value)
            else:
                print '{}: ...'.format(key)
        logging.critical(res)
    except:
        import traceback
        traceback.print_exc()
        logging.critical('Calculation is failed')

if __name__ == '__main__':
    main()
